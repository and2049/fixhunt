let callCount = 0;
const size = {get value() { callCount++; return 5; }};
class Foo {
  constructor(x) {
    console.log('Foo arg:', x, 'calls:', callCount);
  }
}
new Foo(5 == size.value);
console.log('After:');
new Foo(size.value == 5);
