/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function (nums) {
    let obj = {};

    nums.forEach(num => {
        if (!obj[num]) {
            obj[num] = 1;
        } else {
            obj[num]++;
        }

    })
    for (let key in obj) {
        if (obj[key] === 1) {
            return key;
        }
    }

};