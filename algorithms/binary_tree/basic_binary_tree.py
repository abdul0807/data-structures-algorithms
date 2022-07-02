# ********************************************
# Created by Mohammed Abdul Qavi on 02/07/22
# ********************************************


class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """
        Return True if the value
        is in the tree, return
        False otherwise.
        """
        current = self.root
        if current:
            while current:
                if current.value == find_val:
                    return True
                else:
                    return self.preorder_search(current, find_val)
        return False

    def print_tree(self):
        """
        Print out all tree nodes
        as they are visited in
        a pre-order traversal.
        """
        output_str = ""
        if self.root:
            output_str += self.preorder_print(
                self.root, output_str + str(self.root.value)
            )
        else:
            output_str += "the tree is empty"

        return output_str

    def preorder_search(self, start, find_val):
        """
        Function to create a recursive search solution.
        """
        if start.left:
            if start.left.value == find_val:
                return True
            else:
                return self.preorder_search(start.left, find_val)
        if start.right:
            if start.right.value == find_val:
                return True
            else:
                return self.preorder_search(start.right, find_val)
        return False

    def preorder_print(self, start, traversal):
        """
        Function used to create a recursive print solution.
        """
        if start:
            if start.left:
                traversal = self.preorder_print(
                    start.left, traversal + "-" + str(start.left.value)
                )
            if start.right:
                traversal = self.preorder_print(
                    start.right, traversal + "-" + str(start.right.value)
                )

        return traversal


if __name__ == "__main__":
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)

    print(tree.search(4))
    print(tree.search(6))

    print(tree.print_tree())

"""
Output

True
False
1-2-4-5-3
"""