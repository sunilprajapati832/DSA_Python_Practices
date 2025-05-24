# and traversal of Singly Linked List
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(node):
    # Iterate till node reaches None
    while node is not None:
        # Print the data
        print(node.data, end=" ")
        node = node.next


if __name__ == "__main__":
    # Linked List 1 -> 2 -> 3
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.next = third
    print_list(head)


"""
"""
# and traversal of doubly Linked List

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def forward_traversal(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()


def backward_traversal(tail):
    curr = tail
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.prev
    print()


if __name__ == "__main__":
    # Linked List 1 <-> 2 <-> 3
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second

    print("Forward Traversal:")
    forward_traversal(head)

    print("Backward Traversal:")
    backward_traversal(third)

"""
"""
# and traversal of Circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(last):
    if last is None:
        return

    head = last.next
    while True:
        print(head.data, end=" ")
        head = head.next
        if head == last.next:
            break
    print()

# Create circular linked list: 2, 3, 4
first = Node(2)
first.next = Node(3)
first.next.next = Node(4)
last = first.next.next
last.next = first

print_list(last)

"""


# Python  program to illustrate creation
# and traversal of doubly circular Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


def forward_traversal(head):
    curr = head
    if head is not None:
        while True:
            print(curr.data, end=" ")
            curr = curr.next
            if curr == head:
                break
    print()


def backward_traversal(head):
    curr = head.prev
    if head is not None:
        while True:
            print(curr.data, end=" ")
            curr = curr.prev
            if curr.next == head:
                break
    print()


if __name__ == "__main__":
    # Create a doubly circular linked list
    # 1 <-> 2 <-> 3 <-> 1
    head = Node(1)
    second = Node(2)
    third = Node(3)

    head.next = second
    second.prev = head
    second.next = third
    third.prev = second
    third.next = head
    head.prev = third

    print("Forward Traversal:")
    forward_traversal(head)

    print("Backward Traversal:")
    backward_traversal(head)