// https://leetcode.com/problems/plus-one/submissions/1080590470/
import java.math.BigInteger;
class Solution {
    public int[] plusOne(int[] digits) {
        String allTogether = Arrays.stream(digits).mapToObj(String::valueOf).collect(Collectors.joining(""));
        BigInteger num = (new BigInteger(allTogether)).add(BigInteger.ONE);
        
        allTogether = num.toString();
        digits = new int[allTogether.length()];
        for(int index = 0; index < allTogether.length(); index++){
            digits[index] = Character.getNumericValue(allTogether.charAt(index));
        }
         
        return digits;
    }
}
