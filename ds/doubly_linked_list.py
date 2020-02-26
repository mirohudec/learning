from typing import Optional


class Node:
    """
    Class representing internal structure for Doubly linked list
    """

    def __init__(self, data: object, prev: Optional['Node'] = None, next: Optional['Node'] = None):
        """
        Create Node

        :param object data: Data saved in the node
        :param Node prev: Reference to the previous Node
        :param Node next: Reference to the next Node
        """
        self.data = data
        self.prev = prev
        self.next = next


class DoublyLinkedList:
    """
    Implementation of Doubly linked list data structure
    """

    def __init__(self):
        """
        Create Doubly linked list
        """
        self.size = 0
        self.head = None
        self.tail = None

    @classmethod
    def from_list(cls):

    def add_last(self, data: object):
        """
        Add data to the end of the list

        :param data: Data to add
        :return:
        """
        if self.is_empty:
            self.head = self.tail = Node(data=data)
        else:
            # add new node to the end of the list, change prev to tail
            self.tail.next = Node(data=data, prev=self.tail)
            self.tail = self.tail.next
        self.size += 1

    def add_first(self, data: object):
        """
        Add data as the first element of the list

        :param data: Data to add
        :return:
        """
        if self.is_empty:
            self.head = self.tail = Node(data=data)
        else:
            # add new node to the start of list as prev node of the head, set next as current head
            self.head.prev = Node(data=data, next=self.head)
            self.head = self.head.prev
        self.size += 1

    def add(self, data: object, index: int):
        """
        Adds data at the specified index.

        :param object data: Data to add
        :param int index: Position of the data in the list
        :return:
        """
        if index < 0 or index > self.size:
            return IndexError()
        elif index == 0:
            self.add_first(data=data)
        elif index == self.size:
            self.add_last(data=data)
        else:
            # check whether the index is closer to head or tail
            if index < round(self.size) / 2:
                #  closer to head
                trav = self.head.next
                position = 1
                while trav:
                    if index == position:
                        node = Node(data=data, prev=trav.prev, next=trav)
                        trav.prev.next = node
                        trav.prev = node
                        break
                    trav = trav.next
                    position += 1
            else:
                # closer to tail
                trav = self.tail
                position = self.size - 1
                while trav:
                    if index == position:
                        node = Node(data=data, prev=trav.prev, next=trav)
                        trav.prev.next = node
                        trav.prev = node
                        break
                    trav = trav.prev
                    position -= 1
        self.size += 1

    def clear(self):
        """
        Remove every element from the list

        :return:
        """
        trav = self.head
        while trav:
            node = trav.next
            trav.prev = None
            trav.next = None
            trav = node
        self.head = None
        self.tail = None
        self.size = 0

    @property
    def is_empty(self) -> bool:
        """
        Checks if the list is empty

        :return: Returns whether the list is empty
        :rtype: bool
        """
        return not bool(self.size)

    def __len__(self):
        return self.size

    def __str__(self):
        output = '['
        trav = self.head
        while trav:
            if trav.next:
                output += f'{trav.data}, '
            else:
                output += f'{trav.data}'
            trav = trav.next
        return output + ']'

    def __iter__(self):
        trav = self.head
        while trav:
            yield trav.data
            trav = trav.next

    def __reversed__(self):
        trav = self.tail
        while trav:
            yield trav.data
            trav = trav.prev
