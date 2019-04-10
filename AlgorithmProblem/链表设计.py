__author__ = 'Darr_en1'


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """

        self.tail = self.head = Node(None)

    def get(self, index):
        """
        Get the value of the index-th Node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        nd = self.head
        for i in range(index + 1):
            nd = nd.next
            if nd is None: return -1
        return nd.val

    def addAtHead(self, val):
        """
        Add a Node of value val before the first element of the linked list. After the insertion, the new Node will be the first Node of the linked list.
        :type val: int
        :rtype: void
        """
        nd = Node(val, self.head.next)
        self.head.next = nd
        if self.tail.val is None: self.tail = nd

    def addAtTail(self, val):
        """
        Append a Node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        self.tail.next = Node(val)
        self.tail = self.tail.next

    def addAtIndex(self, index, val):
        """
        Add a Node of value val before the index-th Node in the linked list. If index equals to the length of linked list, the Node will be appended to the end of linked list. If index is greater than the length, the Node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        nd = self.head
        for i in range(index):
            nd = nd.next
            if nd is None:
                return
        new = Node(val, nd.next)
        nd.next = new
        if self.tail == nd:
            self.tail = new

    def deleteAtIndex(self, index):
        """
        Delete the index-th Node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        nd = self.head
        for i in range(index):
            nd = nd.next
            if nd is None: return
        if self.tail == nd.next: self.tail = nd
        if nd.next: nd.next = nd.next.next


if __name__ == '__main__':
    mylinklist = MyLinkedList()
    mylinklist.addAtHead(4)
    mylinklist.addAtHead(6)
    mylinklist.addAtHead(9)
    mylinklist.addAtHead(11)

    mylinklist.addAtIndex(2,34)
