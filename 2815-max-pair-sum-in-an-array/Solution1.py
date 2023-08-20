# https://leetcode.com/problems/max-pair-sum-in-an-array/submissions/1026207781/
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        maxSum = -1

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                num1, num2 = nums[i], nums[j]
                maxD1 = self.maxDigit(num1)
                if maxD1 != -1 and maxD1 == self.maxDigit(num2):
                    if num1 + num2 > maxSum:
                        maxSum = num1 + num2

        return maxSum

    def maxDigit(self, num):
        max = -1
        for digit in str(num):
            if int(digit) > max:
                max = int(digit)

        return max
