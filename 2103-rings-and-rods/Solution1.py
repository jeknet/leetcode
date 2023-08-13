# https://leetcode.com/problems/rings-and-rods/submissions/1020598927/
class Solution:
    def __init__(self):
        self.colors = {"R":1, "G":2, "B":4}

    def countPoints(self, rings: str) -> int:
        res = {}
        count = set()

        ring, color = 0, 0
        for i in range(len(rings) -1, -1, -1): 
            if i % 2 == 1:
                ring = rings[i]
                if ring not in res:
                    res[ring] = 0
            else:
                color = rings[i] 

                res[ring] = res[ring] | self.colors[color]
                if res[ring] == 7:
                    count.add(ring)
           
        return len(count)
