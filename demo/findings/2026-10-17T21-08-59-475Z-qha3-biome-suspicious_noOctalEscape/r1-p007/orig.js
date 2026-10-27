let s = "\251";
console.log(s?.length ?? 'null');
s = '';
console.log(s?.length ?? 'empty');
s = null;
console.log(s?.length ?? 'null');
