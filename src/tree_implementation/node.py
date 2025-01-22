class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.height=1
        self.value = value

    def __str__(self) -> str:
        if self.right and not self.left:
            return f"Value: {self.value}\nleft: doesn`t exist\nright: {self.right.value}"
        elif self.left and not self.right:
            return f"Value: {self.value}\nleft: {self.left.value}\nright: doesn`t exist"
        else: return f"Value: {self.value}\nleft: doesn`t exist\nright: doesn`t exist"
    