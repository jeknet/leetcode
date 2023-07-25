# https://leetcode.com/problems/goal-parser-interpretation/submissions/1003724463/

import re

class Solution:
    def interpret(self, command: str) -> str:
        return re.sub("\(al\)", "al", re.sub("\(\)","o", command))
