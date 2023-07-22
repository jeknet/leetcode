# https://leetcode.com/problems/defanging-an-ip-address/submissions/1001130765/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return "".join(x if x != "." else "[.]" for x in address)
