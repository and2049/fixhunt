try {
  throw new Error('value: ' + 12_345);
} catch (e) {
  console.log(e.message);
}
