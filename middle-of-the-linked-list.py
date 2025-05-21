# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Function to create a linked list from a Python list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to print the linked list from a given node
def print_linked_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

# ----------- MAIN TEST ----------------
if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6]  # Test list
    head = create_linked_list(values)

    sol = Solution()
    mid_node = sol.middleNode(head)

    print("Middle node and onward:")
    print_linked_list(mid_node)
