// https://leetcode.com/problems/find-maximum-number-of-string-pairs/submissions/
/**
 * @param {string[]} words
 * @return {number}
 */
var maximumNumberOfStringPairs = function(words) {
    const reversed = new Map();
    let counter = 0;

    for(let word of words){
        if(reversed.has(word)){
            counter += 1;
            reversed.delete(word);
        }else{
            let reverseString = word.split("").reduce((acc, letter) => letter + acc, "");
            reversed.set(reverseString, true); 
        }
    }
 
    return counter;
};
