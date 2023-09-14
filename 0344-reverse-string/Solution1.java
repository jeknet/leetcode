// https://leetcode.com/problems/reverse-string/submissions/1048905859/
class Solution {
    public void reverseString(char[] s) {
        int last = s.length -1;
        int start = 0;
        while(start<=last){
            char temp = s[start];
            s[start++] = s[last];
            s[last--] = temp;
        }
    }
}
