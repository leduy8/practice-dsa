from queue import Queue
import queue
import sys


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None


class Tree:
    def __init__(self) -> None:
        self.root = None

    def is_empty(self):
        return self.root is None

    def is_leaf_node(self, node):
        return node.left is None and node.right is None

    def insert(self, value):
        node = Node(value)

        if self.is_empty():
            self.root = node
            return

        current = self.root
        while True:
            if value <= current.value:
                if current.left is None:
                    current.left = node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = node
                    return
                current = current.right

    def find(self, value) -> bool:
        current = self.root

        while current is not None:
            if value == current.value:
                return True

            current = current.left if value < current.value else current.right

        return False

    def pre_order_traversal(self):
        self.__pre_order_traversal_impl(self.root)

    def __pre_order_traversal_impl(self, root):
        # ? Root, left, right
        if root:
            print(root.value)
            self.__pre_order_traversal_impl(root.left)
            self.__pre_order_traversal_impl(root.right)

    def in_order_traversal(self):
        self.__in_order_traversal_impl(self.root)

    def __in_order_traversal_impl(self, root):
        # ? Left, root, right
        if root:
            self.__in_order_traversal_impl(root.left)
            print(root.value)
            self.__in_order_traversal_impl(root.right)

    def post_order_traversal(self):
        self.__post_order_traversal_impl(self.root)

    def __post_order_traversal_impl(self, root):
        # ? Left, right, root
        if root:
            self.__post_order_traversal_impl(root.left)
            self.__post_order_traversal_impl(root.right)
            print(root.value)

    def breadth_first_traversal(self):
        # ? Level order
        queue = Queue(maxsize=30)
        queue.put(self.root)

        while queue._qsize() > 0:
            current = queue.get()
            print(current.value)
            if current.left:
                queue.put(current.left)
            if current.right:
                queue.put(current.right)

    def height(self):
        if self.is_empty():
            return -1

        return self.__calc_height(self.root)

    def __calc_height(self, root):
        if self.is_leaf_node(root):
            return 0

        return 1 + max(self.__calc_height(root.left), self.__calc_height(root.right))

    # O(n)
    def min(self):
        if self.is_empty():
            return -1

        return self.__find_min(self.root)

    def __find_min(self, root):
        if self.is_leaf_node(root):
            return root.value

        left = self.__find_min(root.left)
        right = self.__find_min(root.right)
        min_of_subtree = left if left <= right else right
        return min(min_of_subtree, root.value)

    # O(logn)
    def min_binary_search_tree(self):
        if self.is_empty():
            return -1

        current = self.root

        while current.left:
            current = current.left

        return current.value

    def equals(self, tree):
        if not tree:
            return False

        return self.__equals(self.root, tree.root)

    def __equals(self, first, second):
        if not first and not second:
            return True

        if first and second:
            return first.value == second.value and self.__equals(first.left, second.left) and self.__equals(first.right, second.right)

        return False

    def is_bst(self):
        if self.is_empty():
            return -1

        return self.__is_bst(self.root, -sys.maxsize, sys.maxsize)

    def __is_bst(self, root, min_boundary, max_boundary):
        if root is None:
            return True

        if root.value < min_boundary or root.value > max_boundary:
            return False

        return self.__is_bst(root.left, min_boundary, root.value - 1) and self.__is_bst(root.right, root.value + 1, max_boundary)

    def get_nodes_at_k_distance(self, k):
        nodes = []
        self.__get_nodes_at_k_distance(self.root, k, nodes)
        return nodes

    def __get_nodes_at_k_distance(self, root, k, nodes):
        if not root:
            return

        if k == 0:
            nodes.append(root.value)
            return

        self.__get_nodes_at_k_distance(root.left, k-1, nodes)
        self.__get_nodes_at_k_distance(root.right, k-1, nodes)

    def size(self):
        nodes = []
        self.__size(self.root, nodes)
        return len(nodes)

    def __size(self, root, nodes):
        if root:
            nodes.append(root.value)
            self.__size(root.left, nodes)
            self.__size(root.right, nodes)

    def count_leaves(self):
        leaves = []
        self.__count_leaves(self.root, leaves)
        return len(leaves)

    def __count_leaves(self, root, leaves):
        if root:
            if self.is_leaf_node(root):
                leaves.append(root.value)
            self.__count_leaves(root.left, leaves)
            self.__count_leaves(root.right, leaves)

    def find_max(self):
        return self.__find_max(self.root)

    def __find_max(self, root):
        if self.is_leaf_node(root):
            return root.value

        left = self.__find_max(root.left)
        right = self.__find_max(root.right)
        max_of_subtree = left if left > right else right
        return max(max_of_subtree, root.value)

    # ? Similar to find, but with recursion
    def contains(self, value):
        return True if self.__contains(self.root, value) else False


    def __contains(self, root, value):
        if root is None or root.value == value:
            return root

        if root.value < value:
            return self.__contains(root.right, value)

        return self.__contains(root.left, value)

    def are_sibling(self, first, second):
        queue = Queue(maxsize=30)
        queue.put(self.root)

        while queue.qsize() > 0:
            current = queue.get()

            if current.left and current.right and (current.left.value == first and current.right.value == second) or (current.left.value == second and current.right.value == first):
                return True
            
            if current.left:
                queue.put(current.left)

            if current.right:
                queue.put(current.right)

        return False

    def get_ancestors(self, value):
        ancestors = []
        self.__get_ancestors(self.root, value, ancestors)
        return f'Ancestors of {value} are {ancestors}.'

    def __get_ancestors(self, root, value, ancestors):
        if root == None:
            return False
        
        if root.value == value:
            return True
    
        if (self.__get_ancestors(root.left, value, ancestors) or self.__get_ancestors(root.right, value, ancestors)):
            ancestors.append(root.value)
            return True
    
        return False


tree = Tree()
tree.insert(7)
tree.insert(4)
tree.insert(9)
tree.insert(1)
tree.insert(6)
tree.insert(8)
tree.insert(10)
# print(tree.find(7))
# print(tree.find(4))
# print(tree.find(9))
# print(tree.find(1))
# print(tree.find(6))
# print(tree.find(8))
# print(tree.find(10))
# print(tree.find(11))
# tree.pre_order_traversal()
# tree.in_order_traversal()
# tree.post_order_traversal()
# tree.breadth_first_traversal()
# print(tree.height())
# print(tree.min())
# print(tree.min_binary_search_tree())

# another = Tree()
# another.insert(7)
# another.insert(4)
# another.insert(9)
# another.insert(1)
# another.insert(6)
# another.insert(8)
# another.insert(10)

# print(tree.equals(another))
# print(tree.is_bst())
# print(tree.get_nodes_at_k_distance(2))
# print(tree.size())
# print(tree.count_leaves())
# print(tree.find_max())
# print(tree.contains(10))
# print(tree.are_sibling(1, 6))
# print(tree.get_ancestors(1))

