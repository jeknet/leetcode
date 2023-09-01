// https://leetcode.com/problems/valid-parentheses/submissions/1037260356/
class Solution {
    Map<String, String> elements = Map.of(")", "(", "}", "{","]","[");

    public boolean isValid(String s) {
        Stack<String> prevs = new Stack<String>();


        for(int i = 0; i < s.length(); i++){
            String element = Character.toString(s.charAt(i));

            if(prevs.size() == 0){
                prevs.push(element);
                continue;
            }
            if(elements.get(element) == null){
                prevs.push(element);
            }else{
                 if(elements.get(element).equals(prevs.peek())){
                        prevs.pop();
                }else{
                    return false;
                }
            }
        }

        return prevs.size() == 0;
        
    }
}
