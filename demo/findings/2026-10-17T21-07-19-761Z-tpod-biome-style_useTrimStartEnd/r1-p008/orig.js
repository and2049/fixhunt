let s = null;
console.log(s?.trimLeft() ?? 'null');
s = '  ok  ';
console.log(s?.trimLeft());
