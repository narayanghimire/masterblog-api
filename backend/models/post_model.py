class PostModel:
    def __init__(self):
        self.posts = [
            {"id": 1, "title": "First post", "content": "This is the first post."},
            {"id": 2, "title": "Second post", "content": "This is the second post."},
        ]

    def get_all_posts(self):
        return self.posts

    def add_post(self, new_post):
        self.posts.append(new_post)

    def delete_post(self, post_id):
        self.posts = [post for post in self.posts if post['id'] != post_id]

    def update_post(self, post_id, updated_data):
        for post in self.posts:
            if post['id'] == post_id:
                post.update(updated_data)
                return post
        return None

    def find_post(self, post_id):
        for post in self.posts:
            if post['id'] == post_id:
                return post
        return None
