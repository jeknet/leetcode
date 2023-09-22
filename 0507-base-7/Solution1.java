// https://leetcode.com/problems/base-7/submissions/1055843486/
class Solution {
    public String convertToBase7(int num) {
        if(num == 0){
            return "0";
        }
        Stack<Integer> changed = new Stack<Integer>();

        int temp = Math.abs(num);
        while(temp > 0){
            changed.push(temp%7);
            temp = (int)(temp/7);
        }

        StringBuilder sb = new StringBuilder();
        if(num<0){
            sb.append("-");
        }
        while(!changed.empty()){
            sb.append(changed.pop());
        }
        return sb.toString();
    }
}
