# https://leetcode.com/problems/build-array-from-permutation/submissions/1005746151/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        print(ans)
        for i in range(len(nums)):
            ans[i] = nums[nums[i]]
 
        return ans
