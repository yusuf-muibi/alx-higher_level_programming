#!/usr/bin/node
const args = process.argv.slice(2);
if (args[0]) {
  // Print the first argument
  console.log(args[0]);
} else {
  // No arguments were passed
  console.log('No argument');
}
