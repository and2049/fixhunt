async function* gen() {
  yield 1;
  let x = await Promise.resolve(2);
  yield {x}; // triggers rule
  yield 3;
}
gen().next().value.then(v1 => {
  gen().next().value.then(v2 => {
    console.log(v1.value, v2.value); // 1, {x:2}
  });
});
