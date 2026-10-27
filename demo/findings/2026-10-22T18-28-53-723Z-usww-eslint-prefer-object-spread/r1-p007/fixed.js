let obj = null;
try {
  ({ ...obj});
} catch (e) {
  console.log(e.name);
}
obj = undefined;
try {
  ({ ...obj});
} catch (e) {
  console.log(e.name);
}
