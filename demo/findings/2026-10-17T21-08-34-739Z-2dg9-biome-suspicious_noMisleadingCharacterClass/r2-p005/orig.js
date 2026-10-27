let re;
try {
  re = /^[Á]$/;
  console.log('created:', re);
  // Simulate what happens if fix removes Á leaving []
  // We can't actually run broken code, so we show the danger
  console.log('risk: if fixed to /^[]$/, it would throw');
} catch (e) {
  console.log(e.name, e.message);
}
