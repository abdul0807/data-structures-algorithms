# *******************************************
# Created by Mohammed Abdul Qavi on 17/06/22
# *******************************************


class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, data):
        """
        Adding new element to the linked list
        :param data: the new element to be added
        :return:
        """
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = data
        else:
            self.head = data

    def insert(self, new_element, position):
        """
        Insert a new element in the linked list for the given position
        Assuming that the position of the first element is 1
        If position is 3, then new element should be place after element 2 and before element 3 in existing list
        :param new_element: the new element to be added to the linked list
        :param position: the position where the element is supposed to be added
        :return:
        """
        assert position >= 1, 'Position is less than 1'

        if position == 1:
            new_element.next = self.head
            self.head = new_element
            return

        count = 1
        current = self.head
        while current:
            if count == position - 1:
                new_element.next = current.next
                current.next = new_element
                return

            current = current.next
            count += 1

        if position >= count:
            raise Exception("Given position is higher than size of linked list")

    def get_position(self, position):
        """
        Get the element in the linked list for a position
        Assuming that the position of the first element is 1
        :param position: the given position
        :return:
        """
        assert position >= 1, 'Position is less than 1'

        self.check_if_empty()

        current = self.head
        count = 1
        while current:
            if count == position:
                return current
            current = current.next
            count += 1

        if position >= count:
            raise Exception("Given position is higher than size of linked list")

    def get_position_by_value(self, value):
        """
        Get the position in the linked list for a value
        Assuming that the position of the first element is 1
        :param value: the given value
        :return:
        """
        self.check_if_empty()

        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next

        return None

    def insert_after_value(self, new_element, value):
        """
        Search for first occurrence of the value and insert the element after the value is found
        :param new_element: the new element to be inserted to the linked list
        :param value: the given value
        :return:
        """
        self.check_empty_list()

        current = self.head
        is_inserted = False
        while current:
            if current.value == value:
                new_element.next = current.next
                current.next = new_element
                is_inserted = True
                break
            current = current.next

        if not is_inserted:
            raise Exception("Given value not found in the linked list")

    def insert_first(self, new_element):
        """
        Insert new element as the head of the LinkedList
        :param new_element: the new element to be added to start of the linked list
        :return:
        """
        if self.head:
            new_element.next = self.head
        self.head = new_element

    def delete(self, value):
        """
        Deleting the first element of a linked list with value matching the given value
        :param value: the value to be deleted
        :return:
        """
        self.check_if_empty()

        current = self.head
        if current.value == value:
            self.head = current.next
            return

        is_deleted = False
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                is_deleted = True
                break
            current = current.next
        if not is_deleted:
            raise Exception('Value not found in the linked list')

    def delete_index(self, index):
        """
        Deleting the element of a linked list based on index
        :param index: the given index
        :return:
        """
        self.check_if_empty()

        current = self.head
        if index == 1:
            self.head = current.next
            return

        is_deleted = False
        count = 1
        while current.next:
            if count == index - 1:
                current.next = current.next.next
                is_deleted = True
                break
            current = current.next
            count += 1
        if not is_deleted:
            raise Exception('Given index is more than the size of linked list')

    def delete_first(self):
        """
        Delete the first (head) element in the LinkedList as return it
        :return:
        """
        deleted = self.head
        if self.head:
            self.head = self.head.next
            deleted.next = None

        return deleted

    def check_if_empty(self):
        """
        Checking if the linked list is empty
        :return:
        """
        if not self.head:
            raise Exception("Empty Linked List")

    def print(self):
        """
        Printing all the elements of the linked list
        :return:
        """
        output_str = ''
        current = self.head
        while current:
            output_str += str(current.value) + '-->'
            current = current.next

        print(output_str)

    def detect_loop(self, remove=False):
        """
        Detecting a loop in linked list using Floyd’s Cycle-Finding Algorithm
        :param remove: True if the detected loop is supposed to be removed else False
        :return: True if a loop is detected / removed, else False
        """
        if self.head is None:
            return
        if self.head.next is None:
            return

        slow_p = self.head
        fast_p = self.head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                if remove:
                    slow_p = self.head

                    while slow_p.next != fast_p.next:
                        slow_p = slow_p.next
                        fast_p = fast_p.next

                    fast_p.next = None  # Remove loop
                return True
        return False


if __name__ == "__main__":
    e1 = Element(1)
    e2 = Element(2)
    e3 = Element(3)
    e4 = Element(4)
    e5 = Element(5)
    e6 = Element(6)
    e7 = Element(7)
    e8 = Element(8)
    e9 = Element(9)

    ll = LinkedList(e1)
    ll.append(e2)
    ll.print()

    ll.append(e3)
    ll.print()
    print(ll.get_position(1).value)
    print(ll.get_position(3).value)

    ll.insert(e4, 3)
    ll.append(e5)
    ll.append(e6)
    ll.append(e7)
    ll.append(e8)
    ll.append(e9)
    ll.print()

    ll.delete(4)
    ll.delete_index(1)
    ll.print()
    print("Loop detected: {}\n".format(ll.detect_loop()))

    print("A loop added to the linked list")
    ll.head.next.next.next.next.next.next.next = ll.head.next.next.next.next
    print("Loop detected: {}\n".format(ll.detect_loop()))

    # detecting and removing the loop
    loop_removal = True
    print("Loop detected and removed: {}\n".format(ll.detect_loop(remove=loop_removal)))
    ll.print()

"""
Output

1-->2-->
1-->2-->3-->
1
3
1-->2-->4-->3-->5-->6-->7-->8-->9-->
2-->3-->5-->6-->7-->8-->9-->
Loop detected: False

A loop added to the linked list
Loop detected: True

Loop detected and removed: True

2-->3-->5-->6-->7-->8-->9-->
"""
