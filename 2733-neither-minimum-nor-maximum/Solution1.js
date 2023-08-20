// https://leetcode.com/problems/neither-minimum-nor-maximum/submissions/1026885445/
/**
 * @param {number[]} nums
 * @return {number}
 */
var findNonMinOrMax = function(nums) {
    if(nums.length <= 2){
        return -1;
    }

    let min = Number.MAX_VALUE;
    let max = 0;
    let minI, maxI = -1;

    nums.forEach(function(num, idx)  { 
        if(num <= min){ 
            min = num;
            minI = idx;
        }
        if(num >= max){
            max = num;
            maxI = idx;
        }
    });
   
    const noLikedIndexes = new Set();
    noLikedIndexes.add(minI);
    noLikedIndexes.add(maxI);

    for(let i = 0; i < nums.length; i++){
        if(!noLikedIndexes.has(i)){
            return nums[i];
        }
    } 
    return -1;
    
};
