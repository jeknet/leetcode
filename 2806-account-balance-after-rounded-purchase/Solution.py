# https://leetcode.com/problems/account-balance-after-rounded-purchase/submissions/1016009835/
class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        to_round = purchaseAmount % 10

        return 100 - ((purchaseAmount + (10 - to_round)) if to_round>=5  else (purchaseAmount - to_round))
