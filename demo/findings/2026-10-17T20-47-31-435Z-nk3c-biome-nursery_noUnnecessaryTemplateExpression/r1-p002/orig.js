function tag(strings, ...values) {
  return { raw: strings, cooked: values };
}
const result = tag`${'hello'}${'world'}`;
console.log('Tagged result:', JSON.stringify(result));
