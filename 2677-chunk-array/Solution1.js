// https://leetcode.com/problems/chunk-array/submissions/1028160794/
/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function(arr, size) {
    let response = [];
    let counter = 0;
    let chunk = [];
    for(let item of arr){
        if(counter == size){
            counter = 0;
            response.push(chunk);
            chunk = [];
        }
        counter++;
        chunk.push(item);
    }
    if(chunk.length > 0){
        response.push(chunk);
    }

    return response;
};
