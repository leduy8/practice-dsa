class AVLNode:
    def __init__(self, value) -> None:
        self.height = 0
        self.value = value
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self) -> None:
        self.root = None

    def is_empty(self):
        return self.root == None

    def insert(self, value):
        self.root = self.__insert(self.root, value)

    def __insert(self, root, value):
        if not root:
            return AVLNode(value)

        if value < root.value:
            root.left = self.__insert(root.left, value)
        else:
            root.right = self.__insert(root.right, value)
        

        self.__set_height(root)

        return self.__balance(root)

    def __balance(self, root):
        if self.__is_left_heavy(root):
            if self.__balance_factor(root.left) < 0:
                root.left = self.__rotate_left(root.left)
            return self.__rotate_right(root)
        elif self.__is_right_heavy(root):
            if self.__balance_factor(root.right) > 0:
                root.right = self.__rotate_right(root.right)
            return self.__rotate_left(root)

        return root

    def __rotate_left(self, root):
        new_root = root.right

        root.right = new_root.left
        new_root.left = root

        self.__set_height(root)
        self.__set_height(new_root)

        return new_root

    def __rotate_right(self, root):
        new_root = root.left

        root.left = new_root.right
        new_root.right = root

        self.__set_height(root)
        self.__set_height(new_root)

        return new_root

    def __set_height(self, node):
        node.height = max(self.__height(node.left), self.__height(node.right)) + 1

    def __is_left_heavy(self, node):
        return self.__balance_factor(node) > 1

    def __is_right_heavy(self, node):
        return self.__balance_factor(node) < -1

    def __balance_factor(self, node):
        return 0 if not node else self.__height(node.left) - self.__height(node.right)

    def __height(self, node):
        return node.height if node else -1


tree = AVLTree()
tree.insert(10)
tree.insert(20)
tree.insert(30)