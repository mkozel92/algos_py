from typing import Any


class Node(object):

    def __init__(self, data: Any):
        self.data = data
        self.next = None


class LinkedList(object):

    def __init__(self):
        self.head = None

    def insert(self, data):
        if not self.head:
            self.head = Node(data)
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def insert_many(self, a_list: list):
        for element in a_list:
            self.insert(element)

    def get_as_list(self):
        elemnts = []
        current = self.head
        while current is not None:
            elemnts.append(current.data)
            current = current.next
        return elemnts

    def __str__(self):
        return str(self.get_as_list())
