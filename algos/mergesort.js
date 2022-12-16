const merge = (arr1, arr2) => {
  let results = [];
  let index1 = 0;
  let index2 = 0;

  while (index1 < arr1.length && index2 < arr2.length) {
    if (arr1[index1] < arr2[index2]) {
      results.push(arr1[index1]);
      index1++;
    } else {
      results.push(arr2[index2]);
      index2++;
    }
  }

  // if (index1 < arr1.length) {
  //   results = [...results, ...arr1.splice(index1)];
  // }

  // if (index2 < arr2.length) {
  //   results = [...results, ...arr2.splice(index2)];
  // }

  while (index1 < arr1.length) {
    results.push(arr1[index1]);
    index1++;
  }
  while (index2 < arr2.length) {
    results.push(arr2[index2]);
    index2++;
  }

  return results;
};

const mergesort = (arr) => {
  if (arr.length <= 1) return arr;

  let mid = Math.floor(arr.length / 2);
  let left = mergesort(arr.slice(0, mid));
  let right = mergesort(arr.splice(mid));

  return merge(left, right);
};

console.log(merge([1, 2, 5, 8, 45, 56, 56], [3, 4, 9, 10, 11]));

let testArray = [
  4, 3, 9, 6, 32, 56, 8, 784, 8786, 43, 11, 12, 23, 14, 15, 16, 18, 17, 90,
];
// console.log(insertionSort(testArray))
// merge([1,2,5,8,45,56,56],[3,4,9,10,11])
console.log(mergesort(testArray));
