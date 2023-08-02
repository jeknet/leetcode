# https://leetcode.com/problems/number-of-arithmetic-triplets/submissions/
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        values = set(nums)

        total = 0

        for num in nums:
            if (num + diff) in values and (num + 2*diff) in values:
                total += 1

        return total
