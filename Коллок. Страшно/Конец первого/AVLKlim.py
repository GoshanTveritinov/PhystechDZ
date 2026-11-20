
`
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def _insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self._insert(root.left, value)
        else:
            root.right = self._insert(root.right, value)

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Right rotation
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Left rotation
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right (Big Right) rotation
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left (Big Left) rotation
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def _delete(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self._delete(root.left, value)
        elif value > root.value:
            root.right = self._delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        root.height = 1 + max(self.height(root.left), self.height(root.right))
        balance = self.balance(root)

        # Right rotation
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right (Big Right) rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left (Big Left) rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, p):
        q = p.right
        B = q.left

        q.left = p
        p.right = B

        p.height = 1 + max(self.height(p.left), self.height(p.right))
        q.height = 1 + max(self.height(q.left), self.height(q.right))

        return q

    def right_rotate(self, p):
        q = p.left
        B = q.right

        q.right = p
        p.left = B

        p.height = 1 + max(self.height(p.left), self.height(p.right))
        q.height = 1 + max(self.height(q.left), self.height(q.right))

        return q

    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def _search(self, root, value):
        if not root:
            return root
        if root.value == value:
            return root
        if root.value < value:
            return self._search(root.right, value)
        else:
            return self._search(root.left, value)

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def delete(self, value):
        self.root = self._delete(self.root, value)
--