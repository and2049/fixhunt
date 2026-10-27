class C {
  static x = (() => { if (false) { return 1; }return 2; })();
}
console.log(C.x);
