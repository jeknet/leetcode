class Solution {
    private int[] options = new int[]{1,2};
    public int climbStairs(int n) {
         int[] values = new int[n+1];
         values[n] = 1;

         for(int i = n; i>=0; i--){
             int value = values[i];
             int added = calculateValue(i, values);
             values[i] = value+added;
         }

         return values[0];
    }

    private int calculateValue(int n, int[] values){
        int total = 0;
        for(int option: options){
            if(n+option < values.length){
                total += values[n+option];
            }
        }
        return total;
    }
}
