# https://leetcode.com/problems/find-center-of-star-graph/submissions/1004912306/
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        elif edges[0][1] == edges[1][0] or edges[0][1] == edges[1][1]:
            return edges[0][1]