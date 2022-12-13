const factorial = (num) => {
  if (num === 1) return num;
  return num * factorial(num - 1);
};

// const fibonacci = (num) => {
//   if (num == 0) return 0;
//   if (num <= 2) return 1;

//   return fibonacci(num - 1) + fibonacci(num - 2);
// };

const fib = (num) => {
  let arr = [0, 1];
  for (let i = 2; i < num + 1; i++) {
    arr.push(arr[i - 2] + arr[i - 1]);
  }
  return arr[num];
};

console.log(factorial(6));
console.log(fib(6));
