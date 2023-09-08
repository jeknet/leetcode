// https://leetcode.com/problems/count-symmetric-integers/submissions/1044290790/
class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int counter = 0;
        for(int i = low; i <= high; i++){
            if(isSymetric(i)){
                counter++;
            }
        }

        return counter;
    }

    private boolean isSymetric(int x){ 
        int left = countDigits(x);
        if(left%2!=0){
            return false;
        }
        left--;
        int right = 0;
        int count = 0; 

        while(right<left){ 
            count += getNthDigit(x, left--) - getNthDigit(x, right++); 
        }  
        return count == 0;
    }

    private int countDigits(int x){
        return 1+(int)Math.floor(Math.log10(x));
    }

    private Integer getNthDigit(int x, int n){
        return (int) Math.floor( (x/Math.pow(10,n))%10 );
    }
}
