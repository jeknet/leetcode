# https://leetcode.com/problems/number-of-beautiful-pairs/submissions/1030996438/
class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        elems = []
        counter = 0

        for i in range(len(nums)-1, -1, -1): 
            counter += sum([1 if self.areBeautiful(str(nums[i])[0], str(val)[-1]) else 0 for val in elems])
            elems.append(nums[i])
  
        return counter
 
    @functools.cache
    def areBeautiful(self, num1, num2):
        return self.gdc(int(num1), int(num2)) == 1

    @functools.cache
    def gdc(self, num1, num2):
        if num1 == num2:
            return num1
        
        if num1 > num2:
            new = num1-num2
            return self.gdc(new, num2) if new > num2 else self.gdc(num2, new)
        else:
            new = num2 - num1
            return self.gdc(new, num1) if new > num1 else self.gdc(num1, new) 
