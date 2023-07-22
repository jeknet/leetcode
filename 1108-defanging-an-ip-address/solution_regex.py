# https://leetcode.com/problems/defanging-an-ip-address/submissions/1001133472/
import re

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return re.sub("\.", "[.]", address) 
