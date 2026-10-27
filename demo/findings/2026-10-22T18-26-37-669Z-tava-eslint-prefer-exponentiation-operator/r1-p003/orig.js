const a = 2, b = 3, c = 4;
// This has three args -> rule should NOT fire
if (false) {
  // Hypothetical broken fix: Math.pow(a, b, c) -> a ** b, c
  // Would be syntax error if uncommented
  // Math.pow(a, b, c);
}
console.log('a:', a, 'b:', b, 'c:', c);
