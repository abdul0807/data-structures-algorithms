# *******************************************
# Created by Mohammed Abdul Qavi on 17/06/22
# *******************************************


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        """
        Adding new element to the double linked list
        :param data: the new element to be added
        :return:
        """
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            new_element.prev = current
            current.next = new_element
        else:
            self.head = new_element

    def insert(self, new_element, position):
        """
        Insert a new element in the double linked list for the given position
        Assuming that the position of the first element is 1
        If position is 3, then new element should be place after element 2 and before element 3 in existing list
        :param new_element: the new element to be added to the double linked list
        :param position: the position where the element is supposed to be added
        :return:
        """
        assert position >= 1, 'Position should be more than 1'
        self.check_empty_list()

        if position == 1:
            self.head = new_element
            return

        current = self.head
        count = 1
        while current:
            if count == position - 1:
                new_element.next, new_element.prev = current.next, current
                current.next = new_element
                return
            current = current.next
            count += 1

        if position >= count:
            raise Exception(
                "The given position is greater than size of double linked list"
            )

    def get_position(self, position):
        """
        Get the element in the double linked list for a position
        Assuming that the position of the first element is 1
        :param position: the given position
        :return:
        """
        self.check_empty_list()

        current = self.head
        count = 1
        while current:
            if count == position:
                return current
            current = current.next
            count += 1

        if position >= count:
            raise Exception("Position is higher than the size of double linked list")

    def get_length(self):
        """
        Finding the length of the double linked list
        :return:
        """
        count = 0

        current = self.head
        while current:
            count += 1
            current = current.next

        return count

    def check_empty_list(self):
        """
        Checking if the double linked list is empty
        :return:
        """
        if not self.head:
            raise Exception("Empty Double Linked List")

    def delete(self, position):
        """
        Deleting the first element of a double linked list with value matching the given value
        :param position: the value to be deleted
        :return:
        """
        assert position >= 1, 'Position should be more than 1'
        self.check_empty_list()

        current = self.head
        if position == 1:
            self.head = current.next
            self.head.prev = None
            return

        count = 1
        while current:
            if count == position:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                return

            current = current.next
            count += 1

        if position >= count:
            raise Exception(
                "The given position is greater than size of double linked list"
            )

    def print_forward(self):
        """
        Printing all the elements of the double linked list in forward direction
        :return:
        """
        out_str = ''

        current = self.head
        while current:
            out_str += str(current.value) + '->'
            current = current.next

        print(out_str)

    def print_backward(self):
        """
        Printing all the elements of the double linked list in backward direction
        :return:
        """
        out_str = ''

        current = self.head
        while current.next:
            current = current.next

        while current:
            out_str += str(current.value) + '->'
            current = current.prev

        print(out_str)


if __name__ == "__main__":
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)

    ll = DoubleLinkedList(e1)
    ll.append(e2)
    ll.append(e3)

    ll.print_forward()
    ll.print_backward()

    print(ll.head.next.next.value)
    print(ll.head.next.next.prev.value)
    print(ll.get_position(3).value)

    ll.insert(e4, 4)
    ll.print_forward()
    ll.print_backward()

    ll.delete(4)
    ll.print_forward()
    ll.print_backward()

    print(ll.get_length())

"""
Output

1->2->3->
3->2->1->
3
2
3
1->2->3->4->
4->3->2->1->
1->2->3->
3->2->1->
3

"""
