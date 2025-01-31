class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def partition_list(self, x):
        if not self.head:
            return

        # Create dummy nodes for the two chains
        less_head = Node(0)
        greater_head = Node(0)

        less = less_head
        greater = greater_head

        current = self.head

        # Traverse the list and partition the nodes
        while current:
            if current.value < x:
                less.next = current
                less = less.next
            else:
                greater.next = current
                greater = greater.next
            current = current.next

        # Connect the two chains
        greater.next = None
        less.next = greater_head.next

        # Update the head of the list
        self.head = less_head.next

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

# Example usage:
ll = LinkedList()
ll.head = Node(3, Node(8, Node(5, Node(10, Node(2, Node(1))))))
ll.print_list()  # Output: 3 -> 8 -> 5 -> 10 -> 2 -> 1 -> None
ll.partition_list(5)
ll.print_list()  # Output: 3 -> 2 -> 1 -> 8 -> 5 -> 10 -> None
