class Base {
  static { let s = 1; console.log('Base static:', s); }
}
class Der extends Base {
  static { let s = 2; console.log('Der static:', s); }
  constructor() { super(); console.log('Der instance:'); }
}
new Der();
