# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head
        
        length = 1
        tail = head
        # getting length of list
        while tail.next:
            tail = tail.next
            length += 1
        
        #avoiding unecessary rotations
        k = k % length

        #checking if rotated list would be same as original list
        if k == 0:
            return head
        
        #stepping to position where we break the link 
        cur = head
        for i in range(length-k-1):
            cur = cur.next

        new_head = cur.next
        cur.next = None
        tail.next = head

        return new_head
        

        