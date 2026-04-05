# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while (curr != None):
            print(curr.val)
            #Changing pointers order
            nxt = curr.next
            curr.next = prev
            #Moving to next node
            prev = curr
            curr = nxt
        #Previous is returned because next ends up to be None
        #as it finishes the list
        return prev

