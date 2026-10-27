let fnResult = null;
if (false) {
} else {
  function helper() { return 99; }
  switch (helper()) {
    case 99:
      fnResult = 'hit';
      break;
  }
}
console.log(fnResult); // should be 'hit'
// After fix: else if(false) { ... } -> helper() still defined and callable in same scope
