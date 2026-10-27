class C {
  #privateField = 42;
  static accessPrivate(obj) {
    try { return obj[\'#private\']; } catch(e) { return 'err: ' + e.name; }
  }
}
const inst = new C();
console.log('access:', C.accessPrivate(inst));
// If rule fixes obj[\'#private\'] to obj.#private, it's valid but not what we want—we want to catch if it breaks
// Actually obj.#private is valid syntax but only accessible from within class; outside is SyntaxError
// So we test: if fix produces obj.#private outside class, it should error
try {
  eval('inst.#private'); // This line may be produced by fix and is invalid outside class
} catch(e) {
  console.log('private access err:', e.name);
}
