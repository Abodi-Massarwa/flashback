from Tree import Node, Tree


class Bst(Tree):

    def __init__(self):
        self.root = None

    def delete(self, val):
        if self.root is None: return None
        return self.delete_rec(self.root, val)

    def insert(self, val):
        if self.root is None:
            self.root = Node(val, None, None)
            return
        self.insert_rec(self.root, val)

    def insert_rec(self, n: Node, val: int):
        if val > n.val:
            if n.right is None:
                n.right = Node(val)
                return
            self.insert_rec(n.right, val)
        if val < n.val:
            if n.left is None:
                n.left = Node(val)
                return

            self.insert_rec(n.right, val)
        # if n is None:
        #     node = Node(val)
        #     n = node
        #     return
        # if val > n.val:
        #     self.insert_rec(n.right, val)
        # else:
        #     self.insert_rec(n.right, val)

    def delete_rec(self, n: Node, val: int):
        if n.val == val:
            return n
        if val > n.val:
            return self.delete_rec(n.right, val)

        return self.delete_rec(n.left, val)

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


if __name__ == '__main__':
    shjra = Bst()
    shjra.insert(1)
    shjra.insert(0)
    shjra.insert(2)
    shjra.insert(3)
    shjra.insert(-1)
    print(shjra.is_in(-4))
    print(shjra.height())
