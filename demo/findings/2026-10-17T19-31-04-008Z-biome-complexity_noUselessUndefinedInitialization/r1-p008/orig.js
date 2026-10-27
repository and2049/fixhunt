function bad() {
  throw new Error('init fail');
}
try {
  let x = bad();
} catch (e) {
  console.log(e.message);
}
