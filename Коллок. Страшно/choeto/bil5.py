"""class Node:
    def __init__(self,value, next=None):
        self.value = value
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def push_front(self,value):
        self.head = Node(value,self.head)
    def pop_front(self,value):
        value = self.head.value
        self.head = self.head.next
        return value
    def find(self,value):
        cur = self.head
        while cur is not None:
            if cur == value:
                return cur
            cur = cur.next
        return None"""
class Stack:
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        raise IndexError
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError
    def is_empty(self):
        return len(self.items) == 0