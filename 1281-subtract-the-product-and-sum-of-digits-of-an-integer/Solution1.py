# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/submissions/1007402435/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod = 1
        sum_ = 0
        for digit in str(n):
            digit = int(digit)
            prod *= digit
            sum_ += digit

        return prod - sum_
