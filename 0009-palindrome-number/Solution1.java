// https://leetcode.com/problems/palindrome-number/submissions/1043936515/
class Solution {
    public boolean isPalindrome(int x) {
        if(x < 0){
            return false;
        }
        List<Integer> digits = digits(x);

        int last = digits.size() -1;
        for(int i = 0; i < digits.size(); i++){
            if(i>last){
                break;
            }
            if(digits.get(i) != digits.get(last)){
                return false;
            }
            last--;
        }

        return true;
    }

    private List<Integer> digits(int x){
        List<Integer> digits = new ArrayList();

        while(x > 0){
            digits.add(x%10);
            x = (int)x/10;
        }

        return digits;
    }
}
