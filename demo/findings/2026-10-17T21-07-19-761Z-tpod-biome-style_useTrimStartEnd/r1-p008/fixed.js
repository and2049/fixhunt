let s = null;
console.log(s?.trimStart() ?? 'null');
s = '  ok  ';
console.log(s?.trimStart());
