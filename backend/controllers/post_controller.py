from flask import Blueprint, jsonify, request

from backend.services.post_service import PostService

post_controller = Blueprint('post_controller', __name__)
post_service = PostService()

@post_controller.route('/api/posts', methods=['GET'])
def get_posts():
    sort_by = request.args.get('sort', '').lower()
    direction = request.args.get('direction', '').lower()
    if sort_by not in ['', 'title', 'content']:
        return jsonify({"error": "Invalid input given. Use 'title' or 'content'."}), 400
    if direction not in ['', 'asc', 'desc']:
        return jsonify({"error": "Invalid input given. Use 'asc' or 'desc'."}), 400
    posts = post_service.get_posts(sort_by=sort_by, direction=direction)
    return jsonify(posts)

@post_controller.route('/api/posts', methods=['POST'])
def add_post():
    new_post_data = request.get_json()
    if not new_post_data or 'title' not in new_post_data or 'content' not in new_post_data:
        return jsonify({"error": "Both 'title' and 'content' are required."}), 400
    new_post = post_service.add_post(new_post_data['title'], new_post_data['content'])
    return jsonify(new_post), 201

@post_controller.route('/api/posts/<int:id>', methods=['DELETE'])
def delete_post(id):
    post = post_service.delete_post(id)
    if post:
        return jsonify({"message": f"Post with id {id} has been deleted successfully."}), 200
    return jsonify({"error": f"Post with id {id} not found."}), 404

@post_controller.route('/api/posts/<int:id>', methods=['PUT'])
def update_post(id):
    updated_data = request.get_json()
    post = post_service.update_post(id, updated_data)
    if post:
        return jsonify(post), 200
    return jsonify({"error": f"Post with id {id} not found."}), 404

@post_controller.route('/api/posts/search', methods=['GET'])
def search_posts():
    title_query = request.args.get('title', '').lower()
    content_query = request.args.get('content', '').lower()
    filtered_posts = post_service.search_posts(title_query, content_query)
    return jsonify(filtered_posts)
