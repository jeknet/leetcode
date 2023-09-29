// https://leetcode.com/problems/monotonic-array/submissions/1062460676/
class Solution {
    public boolean isMonotonic(int[] nums) {
        if(nums.length < 2){
            return true;
        }
        boolean up = isUp(nums);
        int i = 0;
        while(i <= nums.length - 2){
            if(up){
                if(nums[i]>nums[i+1]){
                   return false;
                }
            }else{
                if(nums[i]<nums[i+1]){
                    return false;
                }
            }
            i++;
        }
        return true;
    }

    private boolean isUp(int[] nums){
        int i = 0;
        int diff = nums[i] - nums[i+1];
        i++;
        while(i < nums.length - 1 && diff == 0){
            diff = nums[i] - nums[i+1];
            i++;
        }

        return diff < 0;
    }
}
