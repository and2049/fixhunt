function f() {
  let results = [];
  switch (tag) {
    case 'a': {
      const re = /ab/g;
      re.lastIndex = 0;
      results.push(re.exec('abab'));
      break;
    }
    case 'b':
      results.push(re ? re.lastIndex : -1);
  }
  return results.join(',');
}
tag = 'a';
console.log(f()); // [ 'ab', index: 0, input: 'abab', groups: undefined ], 2
// After fix: re is not defined in case 'b' → ReferenceError
