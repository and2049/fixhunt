export { T } from 'typescript:/dummy';
// Biome may flag and try: export { type T } from ... -> invalid
// Simulate effect:
let got = undefined;
try {
  // This line would be broken by fix
  got = 1;
} catch (e) {
  got = e;
}
console.log(typeof got);
