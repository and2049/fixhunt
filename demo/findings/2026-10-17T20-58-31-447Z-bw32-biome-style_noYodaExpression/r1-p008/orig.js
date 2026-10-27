let side = 0;
const obj = {
  valueOf() {
    side += 1;
    return 42;
  }
};
let value = 42;
if ("" + obj == value) {
  console.log('equal, side=', side);
}
side = 0;
if (value == "" + obj) {
  console.log('equal swapped, side=', side);
}
