class C {
  static dir = import.meta.dirname;
  static log() {
    return C.dir;
  }
}
console.log(C.log());
