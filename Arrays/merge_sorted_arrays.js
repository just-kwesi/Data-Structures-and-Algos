//merge two sorted arrays
//[0,3,4,31], [4,6,30]
// should give [0,3,4,4,6,30,31]

const mergeSortedArrays = (array1, array2) => {
  const mergedArray = [];
  let arr1Index = 0;
  let arr2Index = 0;

  while (mergedArray.length < array1.length + array2.length) {
    let arr1Num = array1[arr1Index];
    let arr2Num = array2[arr2Index];

    if (arr1Index === array1.length && arr2Index < array2.length) {
      mergedArray.push(arr2Num);
      arr2Index++;
      continue;
    } else if (arr2Index === array2.length && arr1Index < array1.length) {
      mergedArray.push(arr1Num);
      arr1Index++;
      continue;
    }

    if (arr1Num > arr2Num) {
      mergedArray.push(arr2Num);
      arr2Index++;
    } else {
      mergedArray.push(arr1Num);
      arr1Index++;
    }
  }

  return mergedArray;
};

let result = mergeSortedArrays([0, 3, 4, 31, 33, 45, 67], [4, 6, 30, 45, 60]);
console.log(result);
