# https://leetcode.com/problems/student-attendance-record-i/submissions/1068980720/
import re

class Solution:
    def checkRecord(self, s: str) -> bool:
        late = re.search("(L){3}", s)
        absents = len(re.findall("(A)", s))

        return late == None and absents < 2
