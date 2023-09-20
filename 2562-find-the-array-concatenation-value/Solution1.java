// https://leetcode.com/problems/find-the-array-concatenation-value/submissions/1054959506/
class Solution {
    public long findTheArrayConcVal(int[] nums) { 
        int start = 0;
        int end = nums.length - 1;
        long total = 0;
        while(start<=end){
            if(start != end){
                total += concatenate(nums[start], nums[end]);
            }else{
                total += nums[start];
            }
            start++;
            end--;
        }
        return total;
    }

    public int concatenate(int num1, int num2){
        String concatenated = String.format("%d%d", num1, num2);
        return Integer.valueOf(concatenated);
    }
}
