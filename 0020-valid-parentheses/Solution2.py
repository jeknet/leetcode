# https://leetcode.com/problems/valid-parentheses/submissions/890939577/
class Solution:
    def isValid(self, s: str) -> bool:
        lazy = {"{":"}", "(":")", "[":"]"}
        queue = []


        for val in s:
            if len(queue) == 0:
                queue.append(val)
                continue
            if val in lazy.keys():
                queue.append(val)
            else:
                expected = lazy.get(queue[-1], None)
                if val == expected:
                    queue.pop() 
                else:
                    queue.append(val)

        return len(queue) == 0
