const s = "\2513"; // octal esc + digit
console.log(s); // should be © + '3'
const t = "\251" + "3";
console.log(t === s ? 'same' : 'diff');
