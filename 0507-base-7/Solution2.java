// https://leetcode.com/problems/base-7/submissions/1055843982/
class Solution {
    public String convertToBase7(int num) {
        if(num == 0){
            return "0";
        }
        return convertToBaseN(num, 7);
    }

    private String convertToBaseN(int num, int base){
        Stack<Integer> changed = new Stack<Integer>();

        int temp = Math.abs(num);
        while(temp > 0){
            changed.push(temp%base);
            temp = (int)(temp/base);
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
