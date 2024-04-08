#!/usr/bin/node

function add(a, b) {
  const sum = a + b;
  console.log(sum);
}

const firstInteger = parseInt(process.argv[2]);
const secondInteger = parseInt(process.argv[3]);

add(firstInteger, secondInteger);
