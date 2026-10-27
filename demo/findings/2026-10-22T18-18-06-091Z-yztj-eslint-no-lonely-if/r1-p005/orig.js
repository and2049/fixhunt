let val = null;
if (val !== undefined) {
  console.log('defined');
} else {
  if (val == null) {
    console.log('nullish');
  }
}
// Change val to undefined to see difference
val = undefined;
if (val !== undefined) {
  console.log('defined');
} else {
  if (val == null) {
    console.log('nullish');
  }
}
