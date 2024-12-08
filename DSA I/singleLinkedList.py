# Initializing a node
class Node:
    def __init__(self, data):
        self.data = data # Assign the given data to the node
        self.next = None # Initializehe next attributeo Null

# Creating a linked list class
class LinkedList:
    def __init__(self):
        self.head = None # Initializing head as None

    # Inserting a new node at the beginning of a linked list
    def insertAtBeginning(self, new_data):
        new_node = Node(new_data) # Create a new node with the given data
        new_node.next = self.head # Point the new node to the current head
        self.head = new_node # Update the head to the new node

    def insertAtEnd(self, new_data):
        new_node = Node(new_data)

        # If the list is empty (head is none), set the head to the new node
        if not self.head:
            self.head = new_node
            return

        # Otherwise, travers the list to find the last node
        last = self.head
        while last.next:
            last = last.next
        
        # Now last is the last node, set it's next to the new node
        last.next = new_node

    def addAfter(self, key, data):
        current = self.head
        while current:
            if current.data == key:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print(None)


if __name__ == '__main__':
    linked_list = LinkedList()
    
    linked_list.insertAtBeginning(10)
    linked_list.insertAtBeginning(20)
    linked_list.insertAtBeginning(30)
    linked_list.insertAtBeginning(40)

    linked_list.insertAtEnd(50)
    linked_list.insertAtEnd(60)
    linked_list.insertAtEnd(70)
    linked_list.insertAtEnd(80)


    linked_list.printList()
