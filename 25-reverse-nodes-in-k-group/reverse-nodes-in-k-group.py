# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        def hasKNodes(node, k):
            while node and k >0:
                node = node.next
                k -= 1
            return k==0
        
        def reverseK(start, k):
            prev = None
            curr = start
            for _ in range(k):
                if not curr:
                    return start, None
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev, curr
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        curr = head

        while curr:
            if not hasKNodes(curr,k):
                break
            group_start = curr
            new_head, next_group = reverseK(curr,k)
            prev_group.next = new_head
            group_start.next = next_group

            prev_group = group_start
            curr = next_group
        return dummy.next