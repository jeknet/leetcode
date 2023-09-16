// https://leetcode.com/problems/valid-palindrome/submissions/1051068753/
class Solution {
    public boolean isPalindrome(String s) {
        List<Character> letters = new ArrayList();
        for(char letter : s.toCharArray()){
            if(isLetter(letter)){
                letters.add(letter<='Z'?(char)(letter+32):letter);
            }
        }
        int start = 0;
        int end = letters.size()-1;
 
        while(start<=end){
            if(letters.get(start++) != letters.get(end--)){
                return false;
            }
        }
        return true;
    }

    private boolean isLetter(char element){
        return (element >= 'a' && element <='z') ||
        (element >= 'A' && element <= 'Z') || 
        (element >= '0' && element <= '9');
    }
}
