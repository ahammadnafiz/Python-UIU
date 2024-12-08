class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __repr__(self):
        return str(self.data)

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def delete_first_node(self):
        if not self.head:  # If the list is empty
            print("The list is empty. Nothing to delete.")
            return

        if self.head == self.tail:  # If there is only one node
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_node(self, data):
        if not self.head:  # If the list is empty
            print("The list is empty. Nothing to delete.")
            return

        # Find the node to delete
        current = self.head
        while current and current.data != data:
            current = current.next

        if not current:  # Node with the given data not found
            print(f"Node with data {data} not found.")
            return

        # Handle the node to delete
        if current == self.head:  # Node is the head
            self.delete_first_node()
        elif current == self.tail:  # Node is the tail
            self.tail = self.tail.prev
            self.tail.next = None
        else:  # Node is in the middle
            current.prev.next = current.next
            current.next.prev = current.prev

        print(f"Node with data {data} has been deleted.")

    def display(self):
        current = self.head
        while current:
            print(current, end=' ')
            if current.next:
                print('<->', end=' ')
            current = current.next
        print(f" <-> None")

# Example usage
double = DoublyLinkedList()
double.add_to_beginning(10)
double.add_to_beginning(20)
double.add_to_beginning(30)
double.add_to_end(-10)

print("Initial list:")
double.display()

print("\nDeleting node with data 20...")
double.delete_node(20)
double.display()

print("\nDeleting node with data 30 (head)...")
double.delete_node(30)
double.display()

print("\nDeleting node with data -10 (tail)...")
double.delete_node(-10)
double.display()

print("\nDeleting node with data 50 (not in list)...")
double.delete_node(50)
double.display()

