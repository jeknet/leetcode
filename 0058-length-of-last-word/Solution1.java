// https://leetcode.com/problems/length-of-last-word/submissions/1046970801/
class Solution {
    public int lengthOfLastWord(String s) {
        boolean shouldCount = false;
        int counter = 0;

        for(int i = s.length()-1; i >=0 ; i--){
            if(' ' != s.charAt(i)){
                shouldCount = true;
                counter++;
            }else{
                if(shouldCount){
                    break;
                }
            }
        }

        return counter;
    }
}
