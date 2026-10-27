function f(a = obj[\'def\'], ...rest) {
  console.log('args length:', arguments.length);
  console.log('func length:', f.length);
  console.log('rest:', rest);
  let o = { def: 42, prop: 24 };
  let sum = o[\'def\'] + o[\'prop\'] + (arguments[0] ?? 0);
  console.log('sum:', sum);
}
f(10);
