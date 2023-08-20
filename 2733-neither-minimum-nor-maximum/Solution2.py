# https://leetcode.com/problems/neither-minimum-nor-maximum/submissions/1026868641/
import heapq

class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        vals = []
        for num in nums:
            heapq.heappush(vals, num)
        if len(vals) > 2:
            val1 = heapq.heappop(vals)
            return heapq.heappop(vals)

        return -1
