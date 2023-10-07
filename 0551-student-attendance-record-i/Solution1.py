# https://leetcode.com/problems/student-attendance-record-i/submissions/883242260/
class Solution:
    def checkRecord(self, s: str) -> bool:
        abscent = False
        late = 0
        
        for record in s:
            if record == 'A':
                late = 0
                if not abscent:
                    abscent = True
                else:
                    return False
            elif record == 'L':
                late += 1
                if late == 3:
                    return False
            else:
                late = 0
        
        return True
