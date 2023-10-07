# https://leetcode.com/problems/student-attendance-record-i/submissions/1068978382/
class Solution:
    def checkRecord(self, s: str) -> bool:
        absentCount= 0
        lateCount = 0
        
        for record in s:
            if record == 'A':
                absentCount += 1
                lateCount = 0
            elif record == 'L':
                lateCount += 1
            elif record == 'P':
                lateCount = 0
           
            if absentCount >= 2 or lateCount >= 3:
                return False

        return True
