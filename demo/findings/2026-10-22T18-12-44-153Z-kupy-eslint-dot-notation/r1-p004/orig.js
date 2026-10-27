class Base { static get baseProp() { return 1; } }
class Derived extends Base {
  static staticProp = 2;
  static {
    try { console.log('static base:', this[\'baseProp\']); } catch(e) { console.log('static err:', e.message); }
    // This line may be fixed but 'super.baseProp' is correct, 'super.baseProp' via dot is fine
    // but we test static access via instance-like syntax
  }
  static test() {
    const obj = { '#private': 99 };
    try { console.log(obj[\'#private\']); } catch(e) { console.log('private err:', e.name); }
    return this[\'staticProp\'];
  }
}
console.log('result:', Derived.test());
