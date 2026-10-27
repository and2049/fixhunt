let result = [];
try {
  result.push(__dirname);
  throw new Error('test');
} catch (e) {
  result.push(e.message);
} finally {
  try {
    result.push(import.meta.dirname);
  } catch (e) {
    result.push('finally error');
  }
}
console.log(result.join('|'));
