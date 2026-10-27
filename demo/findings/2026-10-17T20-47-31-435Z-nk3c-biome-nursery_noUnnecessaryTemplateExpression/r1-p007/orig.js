const obj = {
  getKey() { return `${'prefix'}${'suffix'`; }
};
const fn = obj.getKey;
console.log('Direct call:', obj.getKey());
try {
  console.log('Extracted call:', fn());
} catch (e) {
  console.log('Error:', e.name, e.message);
}
