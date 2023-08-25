# https://leetcode.com/problems/number-of-beautiful-pairs/submissions/1030985633/
import math
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        elems = []
        counter = 0

        for i in range(len(nums)-1, -1, -1): 
            counter += sum([1 if self.areBeautiful(nums[i], val) else 0 for val in elems])
            elems.append(nums[i])
  
        return counter

    def areBeautiful(self, num1, num2):
        first = str(num1)[0]
        last = str(num2)[-1]

        return math.gcd(int(first), int(last)) == 1
