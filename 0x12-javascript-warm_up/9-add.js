#!/usr/bin/node
function add (a, b) {
  const t = a + b;
  console.log(t);
}

add(Number(process.argv[2]), Number(process.argv[3]));
