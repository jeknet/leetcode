# https://leetcode.com/problems/longest-even-odd-subarray-with-threshold/submissions/
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        l, r = 0,0
        inSeq = True, False
        module = 0
        counter = 0

        for idx, num in enumerate(nums):
            if num > threshold:
                module = 0
                inSeq = False
                continue

            modRes = num % 2
            isEven = modRes == 0

            if modRes == module and not inSeq:
                l, r = idx, idx
                inSeq = True
                module = 1
            elif modRes == module and inSeq:
                r = idx
                module = 1 if isEven else 0
            else:
                l,r = idx, idx
                module = 1 if isEven else 0
                inSeq = True if isEven else False

           
            counter = max(counter, r - l + 1 if inSeq else 0)

        return counter
