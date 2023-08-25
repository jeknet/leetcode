// https://leetcode.com/problems/is-object-empty/submissions/1031610914/
/**
 * @param {Object | Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    for(let prop in obj){
        return false;
    }
    return true;
};
