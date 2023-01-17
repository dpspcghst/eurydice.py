from random import randint # let's make this interesting

one = randint(1, 42)
two = randint(1, 42)
three = randint(1, 42)
four = randint(1, 42)
five = randint(1, 42)
six = randint(1, 42)
seven = randint(1, 42)

class Node():
    """
    """

    def __init__(self, data):
        """
        """

        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        """
        Compare the new value with the parent node.
        """

        if self.data:

            if data < self.data:

                if self.left is None:
                    self.left = Node(data)

                else:
                    self.left.insert(data)

            elif data > self.data:

                if self.right is None:
                    self.right = Node(data)

                else:
                    self.right.insert(data)

            else:
                self.data = data
    
    def print_tree(self):
        """
        Print the tree.
        """

        if self.left:
            self.left.print_tree()

        print(self.data)

        if self.right:
            self.right.print_tree()

    def in_order_traversal(self, root):
        """
        Left -> Root -> Right
        """

        result = []

        if root:
            result = self.in_order_traversal(root.left)
            result.append(root.data)
            result = result + self.in_order_traversal(root.right)

        return result

    def preorder_traversal(self, root):
        """
        Root -> Left -> Right
        """

        result = []

        if root:
            result.append(root.data)
            result = result + self.preorder_traversal(root.left)
            result = result + self.preorder_traversal(root.right)

        return result

    def post_order_traversal(self, root):
        """
        Left -> Right -> Root
        """

        result = []
        if root:
            result = self.post_order_traversal(root.left)
            result = result + self.post_order_traversal(root.right)
            result.append(root.data)

        return result

if __name__ == "__main__":
    """
    Use the insert method to add nodes.
    """
    root = Node(one)
    root.insert(two)
    root.insert(three)
    root.insert(four)
    root.insert(five)
    root.insert(six)
    root.insert(seven)
    root.print_tree()
    print(root.in_order_traversal(root))
    print(root.preorder_traversal(root))
    print(root.post_order_traversal(root))
