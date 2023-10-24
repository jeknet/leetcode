# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/submissions/1083023467/
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = None

        for num in nums:
            if num == 1:
                if count != None and count < k:
                    return False
                count = 0
            else:
                count = count if count == None else count + 1

        return True
