# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/submissions/1093593212
import heapq

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        vals = []

        for num in nums:
            heapq.heappush(vals, num * -1)

        first = heapq.heappop(vals) * -1
        second = heapq.heappop(vals) * -1

        return (first - 1) * (second - 1)
