let val = 0;
const obj = {
  get x() {
    val++;
    return 5;
  }
};
if (\"5\" == obj.x) console.log('equal'); // rule triggers, val increments once
console.log('val:', val);
