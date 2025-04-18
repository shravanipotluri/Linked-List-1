# Time Complexity: O(n)
# Space Complexity: O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No


from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head 
        fast = head
        flag = False
        while(fast is not None and fast.next is not None):
            slow= slow.next
            fast = fast.next.next

            if slow == fast:
                flag = True
                break
        
        if not flag:
            return None
        slow = head
        while(slow != fast):
            slow = slow.next
            fast = fast.next
        return slow