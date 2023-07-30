# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/1007438946/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedList = sorted(nums)

        count = {}

        for idx, number in enumerate(sortedList):
            if number not in count:
                count[number] = idx

        return [count[x] for x in nums]
