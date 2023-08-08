// https://leetcode.com/problems/number-of-employees-who-met-the-target/submissions/1015860295/
class Solution {
    public int numberOfEmployeesWhoMetTarget(int[] hours, int target) {
        return (int) Arrays.stream(hours).filter(item -> item >= target).count();
    }
}
