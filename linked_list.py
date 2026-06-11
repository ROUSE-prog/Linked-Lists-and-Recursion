class Node:
    """
    Represents a single node in the linked list.
    
    Each node stores:
    - data: the value held by the node
    - next: reference to the next node
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    A simple singly linked list implementation.

    This class demonstrates recursive techniques for:
    - summing values
    - searching nodes
    - reversing pointers
    """

    def __init__(self):
        self.head = None

    def insert_at_front(self, data):
        """
        Insert a new node at the beginning of the list.

        Time Complexity: O(1)
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Insert a new node at the end of the list.

        Time Complexity: O(n)
        because we must traverse the list to find the tail node.
        """
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = new_node

    def recursive_sum(self):
        """
        Recursively calculate the sum of all node values.

        Recursion is used here to demonstrate elegant traversal
        through each node without using loops.
        """

        def helper(node):

            # BASE CASE:
            # If we reach the end of the list, return 0.
            if node is None:
                return 0

            # RECURSIVE CASE:
            # Add the current node's data
            # and continue traversing the list.
            return node.data + helper(node.next)

        return helper(self.head)

    def recursive_search(self, target):
        """
        Recursively search for a target value in the linked list.

        Recursion provides a clean way to move node-by-node
        until the target is found or the list ends.
        """

        def helper(node):

            # BASE CASE:
            # Reached end of list without finding target.
            if node is None:
                return False

            # BASE CASE:
            # Target found.
            if node.data == target:
                return True

            # RECURSIVE CASE:
            # Continue searching the next node.
            return helper(node.next)

        return helper(self.head)

    def recursive_reverse(self):
        """
        Reverse the linked list using recursion.

        This method demonstrates recursive pointer manipulation
        by reversing links one node at a time.
        """

        def helper(current, previous):

            # BASE CASE:
            # Once current becomes None,
            # previous will be the new head.
            if current is None:
                return previous

            # Save next node before changing pointers.
            next_node = current.next

            # Reverse the pointer direction.
            current.next = previous

            # RECURSIVE CASE:
            # Move forward through the list.
            return helper(next_node, current)

        self.head = helper(self.head, None)

