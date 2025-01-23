class Comment():
    def __init__(self, comment, author) -> None:
        self.comment=comment
        self.author=author
        self.is_deleted=False
        self.replies=[]

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.is_deleted=True
        self.comment="This reply was deleted"

    def display(self, indent=0):
        
        print(" " * indent + (f"[DELETED] {self.comment}" if self.is_deleted else f"{self.author}: {self.comment}"))
        for reply in self.replies:
            reply.display(indent + 4)
