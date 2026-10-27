
class C {
  ['0b1010'] = 'not a literal key'; // string, not number — rule should not fire
}
const c = new C();
console.log(Object.hasOwn(c, '0b1010') ? c['0b1010'] : 'missing');
