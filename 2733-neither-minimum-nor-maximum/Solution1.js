// https://leetcode.com/problems/neither-minimum-nor-maximum/submissions/1026902189/
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

    nums.forEach(function(num, idx)  { 
        if(num <= min){ 
            min = num; 
        }
        if(num >= max){
            max = num; 
        }  
    });

    for(let num of nums){ 
        if(num != min && num != max){
            return num;
        } 
    } 

    return -1;
};
