class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # INSERTION METHODS
    def insert_at_beginning(self, data):
        """Insert a new node at the beginning of the list"""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """Insert a new node at the end of the list"""
        new_node = Node(data)
        
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_after(self, prev_data, data):
        """Insert a new node after a given node value"""
        # Find the node with prev_data
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        
        if not current:
            print(f"Node with data {prev_data} not found")
            return
        
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def insert_at_position(self, position, data):
        """Insert a new node at a specific position"""
        # If position is 0 or 1, insert at beginning
        if position <= 1:
            self.insert_at_beginning(data)
            return
        
        new_node = Node(data)
        current = self.head
        
        # Traverse to the position before insertion
        for _ in range(position - 2):
            if not current:
                print("Position out of range")
                return
            current = current.next
        
        if not current:
            print("Position out of range")
            return
        
        new_node.next = current.next
        current.next = new_node

    # DELETION METHODS
    def delete_first_node(self):
        """Delete the first node of the list"""
        if not self.head:
            return
        self.head = self.head.next

    def delete_last_node(self):
        """Delete the last node of the list"""
        if not self.head:
            return
        
        if not self.head.next:
            self.head = None
            return
        
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_by_value(self, value):
        """Delete first occurrence of a node with specific value"""
        # If list is empty
        if not self.head:
            return
        
        # If head needs to be removed
        if self.head.data == value:
            self.head = self.head.next
            return
        
        # Search for the node to delete
        current = self.head
        while current.next:
            if current.next.data == value:
                current.next = current.next.next
                return
            current = current.next

    def delete_at_position(self, position):
        """Delete node at a specific position"""
        # If list is empty
        if not self.head:
            return
        
        # If deleting first node
        if position <= 1:
            self.head = self.head.next
            return
        
        current = self.head
        for _ in range(position - 2):
            if not current.next:
                print("Position out of range")
                return
            current = current.next
        
        # Check if position is valid
        if not current.next:
            print("Position out of range")
            return
        
        current.next = current.next.next

    def delete_kth_from_end(self, k):
        """Delete the kth node from the end"""
        # Use two-pointer technique
        slow = fast = self.head
        
        # Move fast pointer k nodes ahead
        for _ in range(k):
            if not fast:
                return  # k is larger than list length
            fast = fast.next
        
        # If fast is None, delete first node
        if not fast:
            self.head = self.head.next
            return
        
        # Move both pointers until fast reaches end
        while fast.next:
            slow = slow.next
            fast = fast.next
        
        # Remove the next node after slow
        slow.next = slow.next.next

    # SEARCH AND FIND METHODS
    def search(self, value):
        """Search for a value in the list"""
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1

    def count_occurrences(self, value):
        """Count occurrences of a specific value"""
        count = 0
        current = self.head
        while current:
            if current.data == value:
                count += 1
            current = current.next
        return count

    # TRANSFORMATION METHODS
    def reverse(self):
        """Reverse the linked list"""
        prev = None
        current = self.head
        
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        self.head = prev

    def sort_bubble(self):
        """Sort the list using bubble sort"""
        if not self.head or not self.head.next:
            return
        
        swapped = True
        while swapped:
            swapped = False
            current = self.head
            
            while current.next:
                if current.data > current.next.data:
                    # Swap data, not nodes
                    current.data, current.next.data = current.next.data, current.data
                    swapped = True
                current = current.next

    # UTILITY METHODS
    def get_length(self):
        """Get the length of the linked list"""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None

    def get_middle_node(self):
        """Get the middle node of the list"""
        if not self.head:
            return None
        
        slow = fast = self.head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def detect_cycle(self):
        """Detect if the list contains a cycle"""
        if not self.head:
            return False
        
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False

    def remove_duplicates(self):
        """Remove duplicate nodes"""
        if not self.head:
            return
        
        seen = set()
        current = self.head
        prev = None
        
        while current:
            if current.data in seen:
                # Duplicate found, remove this node
                prev.next = current.next
            else:
                seen.add(current.data)
                prev = current
            current = current.next

    def rotate(self, k):
        """Rotate the list k times to the right"""
        if not self.head or k == 0:
            return
        
        # Find length
        length = self.get_length()
        k = k % length  # Normalize rotation
        
        if k == 0:
            return
        
        # Find new head and break point
        current = self.head
        for _ in range(length - k - 1):
            current = current.next
        
        # Rearrange links
        new_head = current.next
        current.next = None
        
        # Connect end to original head
        end = new_head
        while end.next:
            end = end.next
        end.next = self.head
        
        self.head = new_head

    def display(self):
        """Display the linked list"""
        if not self.head:
            print("List is empty")
            return
        
        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("NULL")

# Demonstration Function
def linked_list_demo():
    print("Linked List Comprehensive Demonstration")
    
    # Create list and demonstrate methods
    ll = LinkedList()
    
    # Insertion
    print("\n1. Insertion Demonstration:")
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_end(30)
    ll.insert_after(20, 25)
    ll.insert_at_position(3, 15)
    print("After Insertions:")
    ll.display()
    
    # Deletion
    print("\n2. Deletion Demonstration:")
    ll.delete_first_node()
    ll.delete_last_node()
    ll.delete_by_value(25)
    print("After Deletions:")
    ll.display()
    
    # Search and Utility
    print("\n3. Search and Utility:")
    print("List Length:", ll.get_length())
    print("Search 15:", ll.search(15))
    print("Middle Node:", ll.get_middle_node().data if ll.get_middle_node() else "No middle node")
    
    # Transformations
    print("\n4. Transformations:")
    print("Original List:")
    ll.display()
    
    ll.reverse()
    print("Reversed List:")
    ll.display()
    
    ll.sort_bubble()
    print("Sorted List:")
    ll.display()
    
    # Extras
    print("\n5. Additional Operations:")
    ll.remove_duplicates()
    print("After Removing Duplicates:")
    ll.display()
    
    ll.rotate(1)
    print("After Rotation:")
    ll.display()

# Run the demonstration
if __name__ == "__main__":
    linked_list_demo()
