switch (0) {
  case 0:
    function f() { return Array(1, 2); }
    break;
}
const arr = f();
console.log(arr.length === 2 && arr[0] === 1);
