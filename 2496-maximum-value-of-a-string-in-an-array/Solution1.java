// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/submissions/1054545890/
class Solution {
    public int maximumValue(String[] strs) {
        int max = 0;
        for(String element : strs){
            int sizeOf = sizeOf(element);
            max = sizeOf > max? sizeOf : max;
        }
        return max;
    }

    private int sizeOf(String element){
        int size = element.length() - 1;
        char[] letters = element.toCharArray();
        int response = 0;
        for(int i = size; i >= 0; i--){
            char letter = letters[i];
            if(letter < '0' || letter > '9'){
                return element.length();
            }
            response += Character.getNumericValue(letter) * Math.pow(10, size - i);
        }

        return response;
    }
}
