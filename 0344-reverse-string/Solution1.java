// https://leetcode.com/problems/reverse-string/submissions/1048427074/
class Solution {
    public void reverseString(char[] s) {
        int last = s.length -1;
        for(int i = 0; i < s.length/2; i++){
            char temp = s[i];
            s[i] = s[last-i];
            s[last-i] = temp;
        }
    }
}
