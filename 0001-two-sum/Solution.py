# https://leetcode.com/problems/two-sum/submissions/888262689/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comp = {}
        for index, value in enumerate(nums):
            if (target-value) in comp:
                return [index, comp[target-value]]
            comp[value] = index

        return []
