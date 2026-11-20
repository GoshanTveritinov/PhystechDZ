class Node:
    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        self.height = 1


class AVL:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def balance(self, node):
        if node is None:
            return 0

        left_height = self.height(node.left)
        right_height = self.height(node.right)

        return left_height - right_height

    def fix_height(self, node):
        node.height = 1 + max(
            self.height(node.left),
            self.height(node.right)
        )

    def insert(self, val):
        self.root = self._insert_recursive(self.root, val)

    def _insert_recursive(self, node, value):
        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        return self.rebalance(node)

    def rebalance(self, node):
        if self.balance(node) < -1:
            if self.balance(node.right) <= 0:
                return self.small_left_rotate(node)
            else:
                return self.big_left_rotate(node)

        elif self.balance(node) > 1:
            if self.balance(node.left) >= 0:
                return self.small_right_rotate(node)
            else:
                return self.big_right_rotate(node)
        self.fix_height(node)
        return node

    def small_left_rotate(self, node):
        new_root = node.right
        new_left_sub = new_root.left

        node.right = new_left_sub
        new_root.left = node

        self.fix_height(node)
        self.fix_height(new_root)

        return new_root

    def small_right_rotate(self, node):
        new_root = node.left
        new_right_sub = new_root.right

        node.left = new_right_sub
        new_root.right = node

        self.fix_height(node)
        self.fix_height(new_root)

        return new_root

    def big_left_rotate(self, node):
        node.right = self.small_right_rotate(node.right)
        return self.small_left_rotate(node)

    def big_right_rotate(self, node):
        node.left = self.small_left_rotate(node.left)
        return self.small_right_rotate(node)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)

        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)

        else:
            if node.left is None:
                return node.right

            if node.right is None:
                return node.left

            successor = node.right

            while successor.left is not None:
                successor = successor.left

            node.value = successor.value

            node.right = self._delete_recursive(
                node.right, successor.value
            )

        return self.rebalance(node)