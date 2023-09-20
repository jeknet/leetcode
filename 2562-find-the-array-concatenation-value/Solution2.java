// https://leetcode.com/problems/find-the-array-concatenation-value/submissions/1054969686/
class Solution {
    public long findTheArrayConcVal(int[] nums) { 
        int start = -1;
        int end = nums.length;
        long total = 0;
        while(++start <= --end){
            total += (start!=end)?concatenate(nums[start], nums[end]):nums[start];
        }
        return total;
    }

    public int concatenate(int num1, int num2){
        int result = 0;
        int digits = 0;
        for(int num : new int[]{num2, num1}){
            while(num >0){
                result += Math.pow(10,digits) * (num%10); 
                num = (int)num/10; 
                digits++;
            }
        }
       
        return result;
    }
}
