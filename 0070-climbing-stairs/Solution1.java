// https://leetcode.com/problems/climbing-stairs/submissions/1045665747/
class Solution {
    private int[] options = new int[]{1,2};
    public int climbStairs(int n) {
        Map<Integer, Integer> old = new HashMap();
        return isGoodStep(n, 0, old);
    }

    private int isGoodStep(int n, int current, Map<Integer, Integer> old){
        if(old.containsKey(current)){
            return old.get(current);
        }
        if(current == n){
            return 1;
        }
        if(current > n){
            return 0;
        }
        int total = 0;
        for(int option : options){
            total += isGoodStep(n, current + option, old);
        }
        old.put(current, total);
        return total;
    }
}
