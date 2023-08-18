# https://leetcode.com/problems/majority-element/submissions/1024409981/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counters = {}
        target = len(nums)//2

        for num in nums:
            counters[num] = counters.get(num, 0) + 1
            if counters[num]>target:
                return num
        
        return None
