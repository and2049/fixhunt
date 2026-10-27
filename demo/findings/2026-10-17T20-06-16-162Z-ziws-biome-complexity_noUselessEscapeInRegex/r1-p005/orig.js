let cache = null;
Object.defineProperty(Object.prototype, 'regex', {
  get() {
    if (!cache) cache = /[\\s]/; // Intended: literal backslash or 's'
    return cache;
  }
});
try {
  console.log('x'.match(/[\\s]/)); // Should match nothing → null
  console.log('x'.match(/[\s]/));   // After fix: matches whitespace → null (still)
                                     // But if we had a string with space...
  console.log(' x'.match(/[\s]/));  // After fix: matches space → [' ']
                                     // Before fix: /[\\s]/ → no match → null
} catch (e) {
  console.log(e.name, e.message);
}
