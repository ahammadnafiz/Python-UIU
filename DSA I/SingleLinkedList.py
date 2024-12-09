
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insertions
    def insertAtBegin(self, data):
        newitem = Node(data)
        newitem.next = self.head
        self.head = newitem

    def insertAtEnd(self, data):
        newitem = Node(data)
        if not self.head:
            self.head = newitem
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newitem

    def insertAtMiddle(self, data, num):
        current = self.head
        while current and current.data != num:
            current = current.next
        if current:
            newitem = Node(data)
            newitem.next = current.next
            current.next = newitem
        else:
            print("Number not found")

    def insertBeforeIndex(self, data, index):
        if index <= 0 or not self.head:
            self.insertAtBegin(data)
            return
        newitem = Node(data)
        current = self.head
        for _ in range(index - 1):
            if not current.next:
                print("Index out of range")
                return
            current = current.next
        newitem.next = current.next
        current.next = newitem

    def insertAfterIndex(self, data, index):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        for _ in range(index):
            if not current:
                print("Index out of range")
                return
            current = current.next
        newitem = Node(data)
        newitem.next = current.next
        current.next = newitem

    # Deletions
    def deleteAtFirst(self):
        if not self.head:
            return
        self.head = self.head.next

    def deleteLast(self):
        if not self.head:
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def deleteAny(self, num):
        if not self.head:
            return
        if self.head.data == num:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != num:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            print("Number not found")

    def delete_kth_position(self, position):
        """Delete the k-th node from the end of the list"""
        length = self.get_length()
        position = length - (position - 1)
        if position < 1 or position > length:
            print("Invalid position")
            return
        if position == 1:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(position - 2):
            current = current.next
        current.next = current.next.next

    # Search
    def search_occurrence(self, value):
        """Search and print all occurrences of a value"""
        if not self.head:
            print("List is empty")
            return
        traveller = self.head
        cnt = 0  # index
        occ = 0  # occurrences
        indices = []
        while traveller:
            if traveller.data == value:
                indices.append(cnt)
                occ += 1
            cnt += 1
            traveller = traveller.next
        print("Indices:", " ".join(map(str, indices)) if indices else "No occurrences found")
        print(f"\nTotal Occurrence of {value} is {occ}")

    def findNodeIndex(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    # Utility
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sort(self):
        if not self.head or not self.head.next:
            return
        current = self.head
        while current:
            index = current.next
            while index:
                if current.data > index.data:
                    current.data, index.data = index.data, current.data
                index = index.next
            current = current.next

    def get_length(self):
        """Get the length of the linked list"""
        cnt = 0
        traveller = self.head
        while traveller:
            cnt += 1
            traveller = traveller.next
        return cnt

    def display(self):
        if not self.head:
            print("List is empty")
            return
        current = self.head
        while current:
            print(f"{current.data} -> ", end="")
            current = current.next
        print("NULL")

# Example Usage
if __name__ == "__main__":
    ll = LinkedList()
    ll.insertAtBegin(10)
    ll.insertAtBegin(20)
    ll.insertAtBegin(30)
    ll.insertAtEnd(40)
    ll.insertAtEnd(50)
    ll.insertAtMiddle(25, 20)

    print("Initial List:")
    ll.display()

    print("\nSearch Occurrence of 20:")
    ll.search_occurrence(20)

    print("\nFind Index of Node with Value 40:")
    print("Index:", ll.findNodeIndex(40))

    print("\nDelete 2nd Node from the End:")
    ll.delete_kth_position(2)
    ll.display()

    print("\nReverse the List:")
    ll.reverse()
    ll.display()

    print("\nSort the List:")
    ll.sort()
    ll.display()

    print("\nLength of List:", ll.get_length())
