class Base { method() { return 'base'; } }
class Der extends Base {}
const d = new Der;
for (let i = 0; i < 1; i++) {
  console.log(d.method());
}
console.log('proto check done');
