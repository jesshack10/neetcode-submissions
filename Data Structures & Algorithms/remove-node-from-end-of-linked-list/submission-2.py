# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #save the head pointer
        h = head
        counter = h
        lenght = 0
        #get the size of the linked list
        while counter:
            lenght += 1
            counter = counter.next
        
        if lenght == n:
            head = head.next
            return head

        #Identify the nth node and remove it
        delNode = h
        prevNode = None
        for k in range(lenght - n):
            prevNode = delNode
            delNode = delNode.next

        #Remove the node
        prevNode.next = delNode.next

        return h
