const val = { valueOf: () => 2, toString: () => '2' };
console.log('Math.pow(val, 3):', val**3);
console.log('val ** 3:', val ** 3);

const sym = Symbol(1);
try {
  console.log(sym**2);
} catch (e) {
  console.log('Math.pow(Symbol) error:', e.name);
}
try {
  console.log(sym ** 2);
} catch (e) {
  console.log('Symbol ** error:', e.name);
}
