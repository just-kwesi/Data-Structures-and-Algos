/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let u = 0;
    let ui = 1;

    for(let i=1;i<nums.length;i++){
        if(nums[u] !== nums[i]){
            u = i;
            nums[ui] = nums[i];
            ui++;
        }
    }
    nums.splice(ui)
};