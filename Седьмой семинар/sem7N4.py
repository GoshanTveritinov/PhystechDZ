class Node:  #Узел
    def __init__(self, val = None):
        self.val = val
        self.pred = None
        self.next = None

class DoubleLinkedList: # 
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

    def append(self, new, index):
        cur = self.head
        new_node = Node(new)
        cur_index = 0
        while cur_index != index-1:
            cur = cur.next
            cur_index += 1
        new_node.next = cur.next
        cur.next = new_node
        new_node.pred = cur
        self.len += 1

    def get(self, index):
        cur = self.head
        cur_index = 0
        while cur_index <= index:
            if cur_index == index:
                return cur.val
            cur_index += 1
            cur = cur.next
    
    def remove(self, val, index):
        cur = self.head
        cur_index = 0
        while cur_index != index-1:
            cur = cur.next
            cur_index += 1

        a = cur.next.val
        cur.next = cur.next.next
        cur.next.next.pred = cur
        self.len -= 1
        return a


    