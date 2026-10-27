const key = 0b1010;
class C {
  [key] = 'dynamic'; // computed, not literal — rule should NOT fire
  method() {
    return this[key];
  }
}
const c = new C();
console.log(c.method()); // Should print 'dynamic'
// If rule incorrectly rewrote [key] to [10], it would still work — but rule doesn't touch computed props
// So this is a near-miss: expect_trigger=false
