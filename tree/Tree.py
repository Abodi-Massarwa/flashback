class Node:
    def __init__(self, val: int = None, left=None, right=None, parent=None) -> object:
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


class Tree:

    def __init__(self):
        self.root = Node()

    def insert(self, val):
        raise NotImplementedError

    def delete(self, val):
        raise NotImplementedError

    def height(self):
        return self.height_rec(self.root)

    def height_rec(self, n) -> int:
        if n is None:
            return (-1)
        return max(self.height_rec(n.left), self.height_rec(n.right)) + 1

    def is_in(self, val) -> bool:

        return self.is_in_rec(self.root, val)

    def is_in_rec(self, n: Node, val: int):
        if n is None or n.val == val:
            if n is None:
                return False
            return True
        if val > n.val:
            return self.is_in_rec(n.right, val)
        return self.is_in_rec(n.left, val)
