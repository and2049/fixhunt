let threw = false;
try {
  const d = __dirname;
} catch (e) {
  threw = true;
}
console.log('threw:', threw);
