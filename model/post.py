from model.user import User

class Post:

    def __init__(self, id: int, title: str, author: User):
        self.id = id
        self.title = title
        self.author = author