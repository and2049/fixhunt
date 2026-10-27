let callCount = 0;
const size = {get value() { callCount++; return 5; }};
class Foo {
  constructor(x) {
    console.log('Foo arg:', x, 'calls:', callCount);
  }
}
new Foo(size.value == 5 );
console.log('After:');
new Foo(size.value == 5);
