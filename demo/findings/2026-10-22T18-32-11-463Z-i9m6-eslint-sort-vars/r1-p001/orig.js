function main() {
  let out = '';
  for (let b = console.log('B') || 2, a = console.log('A') || b * 2; out += a + ','; ) {
    break;
  }
  return out.slice(0, -1);
}
console.log(main());
