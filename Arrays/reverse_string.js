// Create a function that reverses a string:
// "Hi my name is Kwesi" should be
// "isewK si eman ym iH"

const reverseStr = (str) => {
  //check the length and type of input recieved
  if (str.length < 1 || typeof str !== "string" || !str) {
    return "Please provide a valid input!!!";
  }

  // create a new array and push the entry of the str array into
  // the new array from the last index
  reversedArr = [];

  for (let i = str.length - 1; i >= 0; i--) {
    reversedArr.push(str[i]);
  }

  // return the array as a string now
  return reversedArr.join("");
};

console.log(reverseStr("Hi my name is Kwesi"));
