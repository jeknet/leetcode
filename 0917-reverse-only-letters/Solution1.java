// https://leetcode.com/problems/reverse-only-letters/submissions/1050428943/
class Solution {
    public String reverseOnlyLetters(String s) {
        List<Character> letters = new ArrayList();

        for(char letter: s.toCharArray()){
            if(isLetter(letter)){
                letters.add(letter);
            }
        }

        int totalLetters = letters.size()-1; 
        StringBuilder response = new StringBuilder();
        for(char letter: s.toCharArray()){
            if(isLetter(letter)){
                response.append(letters.get(totalLetters--));
            }else{
                response.append(letter);
            }
        }

        return response.toString();
        
    }

    private Boolean isLetter(char letter){
        return (letter >= 'A' && letter <= 'Z') ||
                (letter >= 'a' && letter <= 'z');
    }

}
