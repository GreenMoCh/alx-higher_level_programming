#!/usr/bin/node

function add(a, b) {
	const add = a + b;
	console.log(add);
}

add(Number(process.argv[2]), Number(process.argv[3]));
