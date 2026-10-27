try {
  throw new Error('value: ' + 12345);
} catch (e) {
  console.log(e.message);
}
