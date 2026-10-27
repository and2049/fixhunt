class C {
  static dir = __dirname;
  static log() {
    return C.dir;
  }
}
console.log(C.log());
