#!/usr/bin/node

const firstArg = process.argv[2];
const convertedNum = parseInt(firstArg);

if (!isNaN(convertedNum)) {
	console.log(`My number: ${convertedNum}`);
} else {
	console.log('Not a number');
}
