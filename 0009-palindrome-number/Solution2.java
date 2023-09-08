// https://leetcode.com/problems/palindrome-number/submissions/1043950629/
class Solution {
    public boolean isPalindrome(int x){
        if(x < 0){
            return false;
        }
        int left = countDigits(x);
        int right = 1; 
        while(left>=right){
            if(getNthDigit(x, left--) != getNthDigit(x, right++)){
                return false;
            }
        }
        return true;
    }

    private int countDigits(int x){
        int count = 0;

        while(x > 0){
            count++;
            x = (int)x/10;
        }
        return count;
    }

    private int getNthDigit(int x, int n){
        int digit = 0;
        for(int i = 0; i < n; i++){
            digit = x%10;
            x = (int)x/10;
        }
        return digit;
    }
}
