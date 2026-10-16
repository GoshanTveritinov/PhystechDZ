class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop() if self.stack else None

from collections import deque


class Node:
    def __init__(self, val = None):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0

    def __contains__(self, val):
        cur = self.head
        while (cur): # До тех пор, пока кур не станет None
            if cur.val == val:
                return True
            else:
                cur = cur.next
        return False

    def append(self, new):
        cur = self.head
        new_node = Node(new)
        if self.head is None:
            self.head = new_node
            self.len += 1
        else:
            while (cur.next):
                cur = cur.next
            cur.next = new_node
            self.len += 1

    def remove(self, val):
        cur = self.head
        last = None
        while (cur):
            if cur.val == val:
                if last is None:
                    self.head = cur.next
                else:
                    last.next = cur.next
                self.len -= 1
                return
            last = cur
            cur = cur.next

sum = lambda x,y: x+y
numbers = [1,2,3,4]
squares = map(lambda x: x**2, numbers)

def even(x):
    return x%2 == 0

print(list( filter(even, [1,2,3,4,5,6])))

print(list( filter(lambda x: (x%2 == 0), [1,2,3,4,5,6])))

