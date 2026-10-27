class C {
  method = () => 'hi';
  static field = {
    // Biome does not trigger here: method not same name as key
    other: this.method
  };
}
console.log(C.field.other());
