class Node:
  def __init__(self,key):
    self.key = key
    self.left = None
    self.right = None
    self.parent = None
class SplayTree:
  def __init__(self):
    self.root = None
  def rotate_left(self,node):
    p = node.parent
    r = node.right
    if p is not None:
      if p.left == node:
        p.left = r
      else:
        p.right = r
    t = r.left
    r.left = node
    node.right = t
    node.parent = r
    r.parent = p
    if node.right is not None:
      node.right.parent = node
  def rotate_right(self,node):
    p = node.parent
    l = node.left
    if p is not None:
      if p.left == node:
        p.left = l
      else:
        p.right = l
    t = l.right
    l.right = node
    node.left = t
    node.parent = l
    l.parent = p
    if node.left is not None:
      node.left.parent = node

  def splay(self,node):
    while node.parent != None:
      p = node.parent
      g = p.parent
      if not g:
        if node == p.left:
          self.rotate_right(p)
        else:
          self.rotate_left(p)
      else:
        if node == p.left and p == g.left:
          self.rotate_right(g)
          self.rotate_right(p)
        elif node == p.right and p == g.right:
          self.rotate_left(g)
          self.rotate_left(p)
        elif node == p.right and p == g.left:
          self.rotate_left(p)
          self.rotate_right(g)
        else:
          self.rotate_right(p)
          self.rotate_left(g)
    self.root = node

  def find(self,key):
    current = self.root
    last = None
    while current:
        last = current
        if key == current.key:
            self.splay(current)
            return current
        elif key < current.key:
            current = current.left
        else:
            current = current.right
    if last:
      self.splay(last)
    return None

  def split(self, key):
    if not self.root:
        return None, None

    self.find(key)
    node = self.root

    if node.key > key:
        left = node.left
        node.left = None

        if left:
            left.parent = None

        return left, node

    else:
        right = node.right
        node.right = None

        if right:
            right.parent = None

        return node, right

  def merge(self, node1, node2):
    if node1:
        node1.parent = None
    if node2:
        node2.parent = None

    if not node1:
        return node2
    if not node2:
        return node1

    self.root = node1

    current = node1
    while current.right:
        current = current.right

    self.splay(current)

    current.right = node2
    node2.parent = current

    return current

  def insert(self,key):
    new_node = Node(key)
    if not self.root:
      self.root = new_node
      return
    t1,t2 = self.split(key)
    if t1 and t1.key == key:
        t1.right = t2
        if t2:
            t2.parent = t1
        self.root = t1
        return
    new_node.left = t1
    if t1:
      t1.parent = new_node
    new_node.right = t2
    if t2:
      t2.parent = new_node
    self.root = new_node

  def delete(self,key):
    node = self.find(key)
    if not node:
      return
    self.root = self.merge(node.left,node.right)