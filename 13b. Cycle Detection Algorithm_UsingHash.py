# A linked list node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


# Function to detect Cycle in a linked list using Hashing
def detectCycle(head):

    curr = head
    s = set()

    # traverse the list
    while curr:

        # return false if we already have seen this node before
        if curr in s:
            return True

        # insert current node into the set
        s.add(curr)

        # move to the next node
        curr = curr.next

    # we reach here if list does not contain any cycle
    return False


# Detect Cycle in a linked list
if __name__ == '__main__':

    head = None
    for i in reversed(range(5)):
        head = Node(i + 1, head)

    # insert cycle
    head.next.next.next.next.next = head.next.next

    if detectCycle(head):
        print("Cycle Found")
    else:
        print("No Cycle Found")
