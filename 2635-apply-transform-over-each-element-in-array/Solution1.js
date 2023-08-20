// https://leetcode.com/problems/apply-transform-over-each-element-in-array/submissions/1026167506/
/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let response = [];
    for(let i = 0; i < arr.length; i++){
        response.push(fn(arr[i], i));
    }
    return response; 
};
