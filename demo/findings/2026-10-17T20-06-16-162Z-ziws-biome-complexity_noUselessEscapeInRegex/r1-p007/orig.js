async function process() {
  const re = /[\\d]/; // Intended: literal backslash or 'd'
  const val = await Promise.resolve('\\');
  if (re.test(val)) {
    return 'matched backslash';
  }
  return 'no match';
}
process().then(console.log);
// Before fix: matches '\\' → 'matched backslash'
// After fix : /[\d]/ matches digits → '\\' is not digit → 'no match'
