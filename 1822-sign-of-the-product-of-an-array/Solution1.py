# https://leetcode.com/problems/sign-of-the-product-of-an-array/submissions/1084101712/
class Solution:
    def arraySign(self, nums: List[int]) -> int:
        val = True 
        for num in nums:
            if num == 0:
                return 0
            val = val == (not num <= 0)

        return 1 if val else -1
