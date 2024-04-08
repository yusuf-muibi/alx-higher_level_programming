#!/usr/bin/node
function add(a, b) {
  const t = a + b;
  console.log(t);
}
const firstInteger = parseInt(process.argv[2]);
const secondInteger = parseInt(process.argv[3]);
add(firstInteger, secondInteger);
