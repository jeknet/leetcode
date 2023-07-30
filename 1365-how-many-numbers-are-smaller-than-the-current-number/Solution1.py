# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/submissions/1007426583/

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        start = 0
        response = []
        for num in nums:
            counter = 0
            for x in nums[start:]:
                counter += 1 if x < num else 0
            response.append(counter)
            
        return response
