// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/submissions/1054689652/
import java.util.regex.Pattern;
import java.util.regex.Matcher;

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
        Pattern pattern = Pattern.compile("^[0-9]*$");
        Matcher matcher = pattern.matcher(element);
        if(matcher.find()){
            return Integer.valueOf(element);
        }
        return element.length();
    }

     
}
