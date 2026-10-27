class Base {
  static { const s = 1; console.log('Base static:', s); }
}
class Der extends Base {
  static { const s = 2; console.log('Der static:', s); }
  constructor() { super(); console.log('Der instance:'); }
}
new Der();
