function f() {
  console.log('start')
  return
}
(function() { console.log('IIFE') })()
// Without fix: ASI inserts ; after return → IIFE runs
// With bad fix: if return removed, no ASI break → syntax error
