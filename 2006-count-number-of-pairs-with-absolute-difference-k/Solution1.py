# https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/submissions/1025254759/
class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        required = [[x + k, x -k] for x in nums]
        appears = [{} for x in range(len(nums))]
        self.countAppears(appears, nums, len(nums)-1)
        counter = 0
       
        for idx, x in enumerate(nums):
            posible = required[idx]
            shown = appears[idx]
            for candidate in posible:
                counter += shown.get(candidate, 0)

        return counter

    def countAppears(self, appears, nums, index):
        if index < 0:
            return
         
        if index == len(nums)-1:
            appears[index][nums[index]] = 1
        else:
            curr = appears[index]
            curr.update(appears[index+1])
            curr[nums[index]] = curr.get(nums[index], 0) + 1
        
        return self.countAppears(appears, nums, index - 1)
