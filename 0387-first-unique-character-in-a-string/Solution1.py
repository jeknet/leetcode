# https://leetcode.com/problems/first-unique-character-in-a-string/submissions/1085737646/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        appear = {}
        no = set()
 
        for index, letter in enumerate(s):
            if letter in appear:
                no.add(letter)
                del appear[letter]
            else:
                if letter not in no:
                    appear[letter] = index
        
        if len(appear) == 0:
            return -1
        
        response = len(s)
        for index in appear.values():
            response = min(index, response)

        return response
