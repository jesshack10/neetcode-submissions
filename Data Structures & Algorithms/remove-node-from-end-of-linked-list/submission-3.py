# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        counter = head
        lenght = 0
        while counter:
            counter = counter.next
            lenght += 1

        if lenght == n:
            return head.next

        delNode = dummy
        prev = None
        for k in range(lenght - n):
            prev = delNode
            delNode = delNode.next
        
        prev.next = delNode.next

        return dummy
        

        

