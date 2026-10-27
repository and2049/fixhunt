function test() {
  LABEL: { const obj = null; return obj?.prop ?? 'default'; }
}
console.log(test());
