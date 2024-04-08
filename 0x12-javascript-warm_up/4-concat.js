#!/usr/bin/node
const args = process.argv.slice(2);
if (args.length !== 2) {
  console.log('Usage: ./printArguments.js <argument1> <argument2>');
} else {
  const argument1 = args[0];
  const argument2 = args[1];

  // Print the formatted output
  console.log(`${argument1} is ${argument2}`);
}
