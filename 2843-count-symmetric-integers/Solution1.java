// https://leetcode.com/problems/count-symmetric-integers/submissions/1044067115/
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
        int right = 1;
        int countLeft = 0;
        int countRight = 0;

        while(right<left){
            countLeft += getNthDigit(x, left--);
            countRight += getNthDigit(x, right++);
        } 
        return countLeft == countRight;
    }

    private int countDigits(int x){
        int count = 0;
        while(x > 0){
            count++;
            x = (int)x/10;
        }
        return count;
    }

    private Integer getNthDigit(int x, int n){
        int digit = 0;
        int counter = 1;

        while(true){
            digit = x%10;
            x = (int)x/10;
            if(counter == n){
                return digit;
            }
            counter++;
        } 
    }
}
