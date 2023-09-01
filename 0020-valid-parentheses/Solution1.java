// https://leetcode.com/problems/valid-parentheses/submissions/1037258298/
class Solution {
    Map<String, String> elements = Map.of(")", "(", "}", "{","]","[");

    public boolean isValid(String s) {
        Stack<String> prevs = new Stack<String>();

        for(int i = 0; i < s.length(); i++){
            String element = Character.toString(s.charAt(i));
            if(elements.get(element) == null){
                prevs.push(element);
            }else{
                if(prevs.size() > 0){
                    if(elements.get(element).equals(prevs.peek())){
                        prevs.pop();
                    }else{
                        return false;
                    }
                }else{ 
                    return false;
                }
            }
        }

        return prevs.size() == 0;
        
    }
}
