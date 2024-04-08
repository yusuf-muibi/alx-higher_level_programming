#!/usr/bin/node

const integers = process.argv.slice(2).map(Number);
const numIntegers = integers.length;

if (numIntegers === 0 || numIntegers === 1) {
  console.log(0);
} else {
  const sortedIntegers = integers.sort((a, b) => b - a);
  const secondBiggest = sortedIntegers[1];
  
  console.log(secondBiggest);
}
