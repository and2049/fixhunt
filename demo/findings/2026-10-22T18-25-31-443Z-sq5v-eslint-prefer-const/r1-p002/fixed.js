class C {
  static { const x = 1; console.log(x); }
}
new C(); // triggers rule on x → becomes const, still logs 1
