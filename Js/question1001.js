const fs = require('fs');
const input = fs.readFileSync(0, 'utf8');
const lines = input.trim().split('\n');

const a = parseInt(lines[0]);
const b = parseInt(lines[1]);

const x = a + b

console.log(`X = ${x}`)