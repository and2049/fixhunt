const code = 'return \\a;';
let result;
try { result = eval(code); } catch(e) { result = e.message; }
console.log(result);
