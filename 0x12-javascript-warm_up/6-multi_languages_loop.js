#!/usr/bin/node

const lines = [
  'C is fun',
  'Python is cool',
  'JavaScript is amazing'
];

let output = '';

for (let i = 0; i < 3; ) {

  output += lines[i];
  output += '\n';
  i++;
}

console.log(output);
