import process from "node:process";
const key = 'version'
let output = process[key]
console.log(typeof output)
output = process[key]
console.log(output)
