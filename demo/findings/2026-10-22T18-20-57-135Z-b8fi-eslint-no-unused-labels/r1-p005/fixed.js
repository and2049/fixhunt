function test() {
  { const obj = null; return obj?.prop ?? 'default'; }
}
console.log(test());
