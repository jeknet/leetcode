# https://leetcode.com/problems/majority-element/submissions/1024410462/
# Following this algorithm
# https://en.wikipedia.org/wiki/Boyer–Moore_majority_vote_algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        m, c = 0, 0
        for num in nums:
            if c == 0:
                m = num
                c = 1
            elif m == num:
                c += 1
            else:
                c -= 1

        return m
