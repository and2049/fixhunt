let obj = null;
let a = undefined;
try {
  console.log({a: a}.a?.()); // triggers rule, prints undefined
} catch (e) {
  console.log(e.name);
}
try {
  console.log({a: a}.a());   // would throw if not guarded
} catch (e) {
  console.log(e.name);
}
