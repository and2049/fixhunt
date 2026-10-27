const obj = {
  get a() {
    if (!obj.seen) {
      obj.seen = true;
      throw new Error('lazy error');
    }
    return 42;
  }
};
let count = 0;
try {
  const x = obj.a; // rule triggers
} catch (e) {
  console.log('first:', e.message);
  count++;
}
try {
  const x = obj.a; // second access
} catch (e) {
  console.log('second:', e.message);
  count++;
}
console.log('count:', count); // 2
