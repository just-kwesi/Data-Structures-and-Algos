// Input: nums = [1,2,3,4,5,6,7], k = 3
// Output: [5,6,7,1,2,3,4]
// Explanation:
// rotate 1 steps to the right: [7,1,2,3,4,5,6]
// rotate 2 steps to the right: [6,7,1,2,3,4,5]
// rotate 3 steps to the right: [5,6,7,1,2,3,4]

// Input: nums = [-1,-100,3,99], k = 2
// Output: [3,99,-1,-100]
// Explanation:
// rotate 1 steps to the right: [99,-1,-100,3]
// rotate 2 steps to the right: [3,99,-1,-100]

var rotate = function (nums, k) {
  let startIndex = k;

  for (let i = 0; i < nums.length - 1; i++) {
    let firstIndex = i % k;
    let secondIndex = startIndex % nums.length;
    console.log(
      `first index: ${firstIndex} second index: ${secondIndex} startIndex: ${startIndex}`
    );
    startIndex++;

    let num = nums[firstIndex];
    nums[firstIndex] = nums[secondIndex];
    nums[secondIndex] = num;
  }
  return nums;
};

let input1 = [1, 2, 3, 4, 5, 6, 7];
let shift1 = 3;
let result = rotate(input1, shift1);

let input2 = [1, 2, 3];
let shift2 = 4;
let result2 = rotate(input2, shift2);
console.log(`1st input: ${input1}, shift: ${shift1} and  ouput${result}`);
console.log(`2st input: ${input2}, shift: ${shift2} and  ouput${result2}`);
