const C = { value: 10 };
export { C };
let sum = 0;
outer: for (let i = 0; i < 2; i++) {
  if (i === 1) break outer;
  sum += C.value;
} finally {
  sum += 5;
}
console.log(sum); // Should be 15: 10 (from i=0) + 5 (finally)
