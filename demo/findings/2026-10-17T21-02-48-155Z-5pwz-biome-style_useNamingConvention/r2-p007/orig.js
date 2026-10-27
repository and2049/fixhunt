class Test {
  #private_field = 42;
  getValue() {
    return this[#private_field]; // This is a syntax error, intentional to show invalid pattern
  }
}
try {
  new Test().getValue();
} catch (e) {
  console.log(e.name, e.message);
}
