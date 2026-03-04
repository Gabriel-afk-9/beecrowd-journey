const fs = require('fs');
const input = fs.readFileSync(0, 'utf8');
const lines = input.trim().split('\n');

const x = parseInt(lines[0]);
const y = parseInt(lines[1]);

const sum = x + y;

console.log(`SOMA = ${sum}`)