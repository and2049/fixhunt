class C {
  static arr;
  static { C.arr = Array(1, 2); }
}
console.log(C.arr.length === 2 && C.arr[0] === 1);
