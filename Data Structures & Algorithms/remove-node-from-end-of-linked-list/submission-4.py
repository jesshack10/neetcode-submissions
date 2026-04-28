# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head
        countH = head
        lenght = 0
        while countH:
            lenght += 1
            countH = countH.next
        
        if n == lenght:
            return head.next

        delNode = dummy
        prev = None
        for k in range(lenght - n):
            prev = delNode
            delNode = delNode.next

        prev.next = delNode.next

        return dummy
        