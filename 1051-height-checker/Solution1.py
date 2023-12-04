# https://leetcode.com/problems/height-checker/submissions/1111857667/
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)

        count = 0
        for i in range(len(heights)):
            count += 1 if heights[i] != expected[i] else 0

        return count
        
