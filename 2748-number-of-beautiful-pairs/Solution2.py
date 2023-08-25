# https://leetcode.com/problems/number-of-beautiful-pairs/submissions/1030994796/
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
 
        return self.gdc(int(first), int(last)) == 1

    def gdc(self, num1, num2):
        if num1 == num2:
            return num1
        
        if num1 > num2:
            new = num1-num2
            return self.gdc(new, num2) if new > num2 else self.gdc(num2, new)
        else:
            new = num2 - num1
            return self.gdc(new, num1) if new > num1 else self.gdc(num1, new) 
