// This is before
/* inline */ var /* comment */ x /* end */ = 1;
// After fix, comment placement may break
if (typeof x === 'number') {
  console.log('ok:', x);
} else {
  console.log('fail');
}
