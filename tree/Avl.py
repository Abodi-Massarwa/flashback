from Tree import Tree
from Tree import Node


class Avl(Tree):
    def __init__(self):
        self.root = None

    def insert(self, val: int):
        self.insert_rec(self.root, val)

    def delete(self, val):
        pass

    def insert_rec(self, n: Node, val: int):
        if self.root is None:
            self.root = Node(val)
            return
        if val > n.val:
            if n.right is None:
                x = Node(val)
                n.right = x
                n.right.parent = n
                # TODO add balance check for rotation purposes if possible
                self.checkBalance(x)

            self.insert_rec(n.right, val)
        elif val < n.val:
            if n.left is None:
                x = Node(val)
                n.left = x
                n.left.parent = n
                # TODO add balance check for rotation purposes if possible
                self.checkBalance(x)
            self.insert_rec(n.left, val)

    def checkBalance(self, x: Node):
        if abs(self.length_rec(x.left) - self.length_rec(x.right)) > 1:
            self.reBalance(x)
            return
        elif x.parent is not None:
            self.checkBalance(x.parent)
        return

    def reBalance(self, node):
        # TODO to determine the type of rotation we're seeking to balance our AVL tree
        if self.length_rec(node.left) - self.length_rec(node.right) > 1:
            if self.length_rec(node.left.left) > self.length_rec(node.left.right):
                node = self.rightRotate(node)
            else:
                node = self.leftRightRotate(node)
        else:
            if self.length_rec(node.right.right) > self.length_rec(node.right.left):
                node = self.leftRotate(node)
            else:
                node = self.rightLeftRotate(node)

    def rightRotate(self, node: Node) -> Node:
        left_child = node.left

        if node.parent is not None:
            left_child.parent = node.parent
            if node.parent.right == node:
                node.parent.right = left_child
            else:
                node.parent.left = left_child
        else:
            left_child.parent = None
            self.root = left_child


        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.parent = node

        left_child.right = node
        node.parent = left_child
        return left_child

    def leftRightRotate(self, node) -> Node:
        pass

    def leftRotate(self, node: Node) -> Node:
        right_child = node.right
        if node.parent is not None:
            right_child.parent = node.parent
            if node.parent.right == node:
                node.parent.right = right_child
            else:
                node.parent.left = right_child
        else:
            right_child.parent = None
            self.root = right_child

        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.parent = node

        else:
            node.right=None

        right_child.left = node
        node.parent = right_child
        return right_child

    def rightLeftRotate(self, node) -> Node:
        pass


if __name__ == '__main__':
    avl = Avl()
    avl.insert(5)
    avl.insert(4)
    avl.insert(3)
    print(avl.root.left.val)
