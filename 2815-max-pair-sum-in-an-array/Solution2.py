# https://leetcode.com/problems/max-pair-sum-in-an-array/submissions/1026223756/
import heapq

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        values = {}
        maxValue = -1

        for num in nums:
            maxDigit = max(str(num))
            if maxDigit not in values: 
                values[maxDigit] = []
            heapq.heappush(values[maxDigit], num * -1)
        
        for value in values.values():
            if len(value)>1:
                val1 = heapq.heappop(value) * -1
                val2 = heapq.heappop(value) * -1
                if val1 + val2 > maxValue:
                    maxValue = val1 + val2
        
        return maxValue
