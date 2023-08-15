# https://leetcode.com/problems/separate-the-digits-in-an-array/submissions/1021572095/
class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        response = []
        for num in nums:
            response.extend(self.getDigits(num))
        return response

    def getDigits(self, num):
        items = []

        while num > 0:
            right_most = num%10
            num = num//10
            items.append(right_most)

        return [items[i] for i in range(len(items)-1, -1, -1)]
