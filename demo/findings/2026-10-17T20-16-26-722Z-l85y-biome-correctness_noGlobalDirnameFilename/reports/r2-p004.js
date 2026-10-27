let result = [];
try {
  result.push(__dirname);
} catch (e) {
  try {
  } catch (e) {
  }
}
console.log(result.join('|'));
