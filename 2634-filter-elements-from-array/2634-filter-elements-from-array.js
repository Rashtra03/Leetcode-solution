/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const filterArr = [];

    for(i=0; i<arr.length; i++){
        if(fn(arr[i], i)){
            filterArr.push(arr[i])
        }
    }
    return filterArr;
};