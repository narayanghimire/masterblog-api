class PostModel:
    """Model class for managing posts data."""

    def __init__(self):
        """Initialize the PostModel with some example posts."""
        self.posts = [
            {"id": 1, "title": "First post", "content": "This is the first post."},
            {"id": 2, "title": "Second post", "content": "This is the second post."},
        ]

    def get_all_posts(self):
        """Return all posts."""
        return self.posts

    def add_post(self, new_post):
        """Add a new post to the posts list."""
        self.posts.append(new_post)

    def delete_post(self, post_id):
        """Delete a post by its ID."""
        self.posts = [post for post in self.posts if post['id'] != post_id]

    def update_post(self, post_id, updated_data):
        """Update a post by its ID with new data."""
        for post in self.posts:
            if post['id'] == post_id:
                post.update(updated_data)
                return post
        return None

    def find_post(self, post_id):
        """Find and return a post by its ID."""
        for post in self.posts:
            if post['id'] == post_id:
                return post
        return None
