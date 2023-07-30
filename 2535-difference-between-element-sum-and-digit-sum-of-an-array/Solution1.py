# https://leetcode.com/problems/difference-between-element-sum-and-digit-sum-of-an-array/submissions/

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elementSum = 0
        digitSum = 0

        for num in nums:
            elementSum += num
            digitSum += sum(self.digits(num))

        return int(math.fabs(elementSum - digitSum))

    def digits(self, num):
        digits = []
        while num > 0:
            val = num %10
            num = num//10
            digits.append(val)

        return digits
