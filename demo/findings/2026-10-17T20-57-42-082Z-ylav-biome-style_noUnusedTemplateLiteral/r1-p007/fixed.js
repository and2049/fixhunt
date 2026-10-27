try {
  const x = "hello"; // triggers rule
  console.log(x);
  throw new Error('from after');
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
console.log('end');
