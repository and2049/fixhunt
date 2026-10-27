if (true) {
  // This comment should be preserved
  if (false) { console.log('inner'); }
}
// After fix, the above becomes: if (true && false) { ... }, losing the comment
console.log('Comment presence affects readability only; no runtime change.');
