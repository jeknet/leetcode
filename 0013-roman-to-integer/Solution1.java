// https://leetcode.com/problems/roman-to-integer/submissions/1034413057/
class Solution {
    private Map<String, Integer> values = Map.of("I",1, "V",5, "X", 10, "L",50,"C",100,"D",500,"M",1000);
    
    public int romanToInt(String s) {
        Integer response = 0;
        Integer temp = 0; 

        for(int i = 0; i < s.length(); i++){
            Integer curr = values.get(Character.toString(s.charAt(i)));
            if(temp == 0){
                temp = curr;
            }else if(temp < curr){
                response += curr - temp;
                temp = 0;
            }else if(temp > curr){
                response += temp;
                temp = curr;
            }else{
                temp += curr;
            }
         }

        return response + temp;
    }
}
