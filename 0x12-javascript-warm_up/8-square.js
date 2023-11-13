#!/usr/bin/node

let i, j;
let row;
const arg = process.argv[2];
const size = parseInt(arg);

if (!isNaN(size)) {
	for (i = 0; i < size; i++) {
		row = '';
		for (j = 0; j < size; j++) {
			row += 'X';
		}
		console.log(row);
	}
} else {
	console.log('Missing size');
}
