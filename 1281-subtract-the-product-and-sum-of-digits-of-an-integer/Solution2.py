# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/1007415962/
import math

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum_ = 0

        power = math.floor(math.log10(n))

        for i in range(power, -1, -1):
            power = int(math.pow(10, i))
            digit = n//power
            n -= digit * power
            prod *= digit
            sum_ += digit

        return prod - sum_
