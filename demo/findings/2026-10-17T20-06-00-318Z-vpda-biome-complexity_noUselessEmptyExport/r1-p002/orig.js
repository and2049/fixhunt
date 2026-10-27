const obj = {};
try {
  delete obj.x;
export {}; // This line triggers the rule
} catch (e) {
  console.log(e.constructor.name + ': ' + e.message);
}
