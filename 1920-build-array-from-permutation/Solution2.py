# https://leetcode.com/problems/build-array-from-permutation/submissions/1005754022/

class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        prevs = {}
        # print(ans)
        for i in range(len(nums)):
            val = nums[i]
            if val in prevs.keys():
                nums[i] = prevs[val]
                prevs[i] = val
                del prevs[val]
            else:
                nums[i] = nums[val]
                prevs[i] = val
 
        return nums
