let called = 0;
function getX() { called++; return 5; }
const y = 3;
if (y < getX()) { // triggers yoda: 3 < getX()
  console.log('first', called); // getX called once
}
called = 0;
if (getX() > y) { // would be fix: getX() > 3
  console.log('second', called); // getX called once
}
