class Node:
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = next


# Please do not change code above.


def lengthOfLoop(head: Node) -> int:
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if fast == slow:
            entry = head
            while entry != slow:
                entry = entry.next
                slow = slow.next
                
            cycleStart = slow
            slow = slow.next
            length = 1
            while cycleStart != slow:
                slow = slow.next
                length += 1
            return length
    
    return 0

