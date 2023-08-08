# https://leetcode.com/problems/number-of-employees-who-met-the-target/submissions/1015864593/
class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return len(list(filter(lambda x: x >= target, hours)))
