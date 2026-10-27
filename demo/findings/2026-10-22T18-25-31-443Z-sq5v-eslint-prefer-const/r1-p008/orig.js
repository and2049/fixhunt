class Base {
  static { let baseInit = 1; console.log('base:', baseInit); }
}
class Derived extends Base {
  static { let derivedInit = 2; console.log('derived:', derivedInit); }
  #x = baseInit + derivedInit; // Error: baseInit not accessible
}
try { new Derived(); } catch(e) { console.log(e.name); }
