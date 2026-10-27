if (false) {
} else {
  /* This comment should stay with the inner if logic */
  if (true) {
    console.log('A');
  }
}
console.log('B');
// After fix: else /* This comment... */ if (true) { ... }
// In minified output, comment may be detached from logic, but we trace execution:
// Should print A then B regardless of comment placement.
