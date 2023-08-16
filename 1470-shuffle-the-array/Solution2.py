# https://leetcode.com/problems/shuffle-the-array/submissions/1023447977/
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return list(self.shuffling(nums, n))
    
    def shuffling(self, nums, n):
        for i in range(n):
            yield nums[i]
            yield nums[i+n]
