// https://leetcode.com/problems/number-of-segments-in-a-string/submissions/1047572526/
class Solution {
    public int countSegments(String s) { 
        int counter = 0;
        boolean isWord = false;

        for(int i = 0; i<s.length(); i++){
            char letter = s.charAt(i);

            if(letter == ' '){
                counter += isWord?1:0;
                isWord = false;
            }else{
                isWord = true;
            }
        }

        return counter+=isWord?1:0;

    }
}
