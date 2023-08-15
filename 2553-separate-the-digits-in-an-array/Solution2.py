# https://leetcode.com/problems/separate-the-digits-in-an-array/submissions/1021581607/
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [digit for elements in self.all(nums) for digit in elements]

    def all(self, nums):
         for num in nums:
            digits = list(self.getDigits(num))
            yield [digits[i] for i in range(len(digits)-1,-1,-1)]

    def getDigits(self, num): 
        while num > 0:
            right_most = num%10
            num = num//10
            yield right_most 
