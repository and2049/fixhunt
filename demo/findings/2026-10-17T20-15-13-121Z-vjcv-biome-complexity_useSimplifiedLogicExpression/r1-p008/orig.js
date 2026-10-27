function tags(strings, ...values) {
  console.log('Values received:', values.map(v => String(v)));
  return strings.raw.join('');
}
const x = undefined;
const result = tags`value: ${x || false}`;
console.log('Result:', result);
// After fix: ${x} → passes undefined, so values[0] is 'undefined'
