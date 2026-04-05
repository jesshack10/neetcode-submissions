# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #To detect a cycle a fast and slow pointer technique can be used
        #Edge case of size 1
        if not head.next:
            return False
            
        f = s = head

        while f and s:
            f = f.next.next
            s = s.next
            if f == s:
                return True
        return False