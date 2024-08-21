from backend.models.post_model import PostModel

class PostService:
    """Service layer for handling post-related operations."""

    def __init__(self):
        """Initialize the PostService with a PostModel instance."""
        self.model = PostModel()

    def get_posts(self, sort_by=None, direction='asc'):
        """Retrieve all posts, optionally sorted by a specified field."""
        posts = self.model.get_all_posts()
        if sort_by and sort_by in ['title', 'content']:
            posts.sort(key=lambda post: post[sort_by].lower(), reverse=(direction == 'desc'))
        return posts

    def add_post(self, title, content):
        """Add a new post with the provided title and content."""
        new_id = max(post['id'] for post in self.model.get_all_posts()) + 1
        new_post = {"id": new_id, "title": title, "content": content}
        self.model.add_post(new_post)
        return new_post

    def delete_post(self, post_id):
        """Delete a post by its ID and return the deleted post."""
        post = self.model.find_post(post_id)
        if post:
            self.model.delete_post(post_id)
            return post
        return None

    def update_post(self, post_id, updated_data):
        """Update an existing post with new data."""
        return self.model.update_post(post_id, updated_data)

    def search_posts(self, title_query=None, content_query=None):
        """Search for posts that match the title or content query."""
        posts = self.model.get_all_posts()
        filtered_posts = []
        for post in posts:
            title_match = title_query.lower() in post['title'].lower() if title_query else False
            content_match = content_query.lower() in post['content'].lower() if content_query else False
            if title_match or content_match:
                filtered_posts.append(post)
        return filtered_posts
