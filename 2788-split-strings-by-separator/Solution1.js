// https://leetcode.com/problems/split-strings-by-separator/submissions/1028109249/
/**
 * @param {string[]} words
 * @param {character} separator
 * @return {string[]}
 */
var splitWordsBySeparator = function(words, separator) {
    let response = [];
    let partial = ""; 
    for(let letter of words.join(separator)){     
        if(letter.localeCompare(separator) != 0){
            partial = partial + letter;
        }else if(partial.length>0){
            response.push(partial);
            partial = "";
        }
    }
    if(partial.length>0){
        response.push(partial);
    }

    return response;
};
