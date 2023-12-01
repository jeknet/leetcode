# https://leetcode.com/problems/linked-list-cycle/submissions/1109909876/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        while True:
            if head is None or head.next is None:
                break
            
            if (head.val, head.next) in visited: 
                return True

            visited.add((head.val, head.next))
 
            head = head.next
         
        return False
        
