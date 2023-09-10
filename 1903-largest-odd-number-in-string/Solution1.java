// https://leetcode.com/problems/largest-odd-number-in-string/submissions/1045162487/
class Solution {
    public String largestOddNumber(String num) { 
        for(int index = num.length()-1; index >= 0; index--){
            if(isOdd(num, index)){
                return num.substring(0, index+1);
            }
        }
        return "";
    }

    private boolean isOdd(String num, int index){
        int temp = Character.getNumericValue(num.charAt(index));
        return temp%2 ==1;
    }
}
