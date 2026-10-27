class C {
  static arr;
  static { C.arr = [1, 2]; }
}
console.log(C.arr.length === 2 && C.arr[0] === 1);
