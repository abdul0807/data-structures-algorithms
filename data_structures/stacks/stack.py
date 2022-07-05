# ********************************************
# Created by Mohammed Abdul Qavi on 05/07/22
# ********************************************


class Empty(Exception):
    """Error attempting to access an element from an empty container."""

    pass


class Stack:
    """
    Implementation of python Stack using list as underlying storage
    """

    def __init__(self):
        self._list = list()

    def push(self, value):
        self._list.append(value)

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._list.pop()

    def push_values(self, values):
        self._list.extend(list(values))

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._list[-1]

    def is_empty(self):
        return len(self._list) == 0

    def __len__(self):
        return len(self._list)

    def print(self):
        if len(self._list) == 0:
            return
        element = self._list.pop()
        print(element, end=' ')
        self.print()
        self.push(element)


if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push_values([2, 3, 4, 5, 6])
    print("Length of Stack is {}".format(len(stack)))
    stack.print()
    print('')
    print(stack.pop())
    stack.print()

"""
Output

Length of Stack is 6
6 5 4 3 2 1 
6
5 4 3 2 1
"""
