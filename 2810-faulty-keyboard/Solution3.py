# https://leetcode.com/problems/faulty-keyboard/submissions/1018025931/
class Solution:
    def finalString(self, s: str) -> str:
        res = collections.deque([])
        forward = True

        for letter in s:
            if letter != "i":
                if forward:
                    res.append(letter)
                else:
                    res.appendleft(letter)
            else:
                forward = False if forward else True

        response = ""

        while len(res) > 0:
            response = response + (res.popleft() if forward else res.pop())
            
        return response
