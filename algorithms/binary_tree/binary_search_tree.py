# ********************************************
# Created by Mohammed Abdul Qavi on 02/07/22
# ********************************************

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        """
        Function to insert a new value into the binary search tree
        """
        current = self.root
        while current:
            if current.value > new_val:
                if current.left is None:
                    new_node = Node(new_val)
                    current.left = new_node
                    break
                else:
                    if current.left.value < new_val:
                        new_node = Node(new_val)
                        new_node.left = current.left
                        current.left = new_node
                        break
                    else:
                        current = current.left
            elif current.value < new_val:
                if current.right is None:
                    new_node = Node(new_val)
                    current.right = new_node
                    break
                else:
                    if current.right.value > new_val:
                        new_node = Node(new_val)
                        new_node.right = current.right
                        current.right = new_node
                        break
                    else:
                        current = current.right

    def search(self, find_val):
        """
        Function will return true if the given value is found in the binary search true.
        return false, if otherwise
        """
        current = self.root
        while current:
            if current.value == find_val:
                return True
            elif current.value > find_val:
                current = current.left
            elif current.value < find_val:
                current = current.right

        return False

    def print_tree(self):
        """
        Print out all tree nodes
        as they are visited in
        a pre-order traversal.
        """
        output_str = ""
        if self.root:
            output_str += self.preorder_print(self.root, output_str + str(self.root.value))
        else:
            output_str += "the tree is empty"

        return output_str

    def preorder_print(self, start, traversal):
        """
        Function to create a recursive print solution.
        """
        if start:
            if start.left:
                traversal = self.preorder_print(start.left, traversal + "-" + str(start.left.value))
            if start.right:
                traversal = self.preorder_print(start.right, traversal + "-" + str(start.right.value))

        return traversal


if __name__ == "__main__":
    tree = BST(4)

    # Insert elements
    tree.insert(2)
    tree.insert(1)
    tree.insert(3)
    tree.insert(5)

    print(tree.print_tree())
    print(tree.search(4))
    print(tree.search(6))

"""
Output

4-3-2-1-5
True
False
"""