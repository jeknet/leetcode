# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1020667535/
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = 0
        for candy in candies:
            if candy > maxCandies:
                maxCandies = candy
        
        return [candy + extraCandies >= maxCandies for candy in candies]
