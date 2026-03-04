const fs = require('fs');
const input = fs.readFileSync(0, 'utf8');
const lines = input.trim().split('\n');

const nota1 = parseFloat(lines[0]);
const nota2 = parseFloat(lines[1]);

const media = ((nota1 * 3.5) + (nota2 * 7.5)) / 11

console.log(`MEDIA = ${media.toFixed(5)}`)