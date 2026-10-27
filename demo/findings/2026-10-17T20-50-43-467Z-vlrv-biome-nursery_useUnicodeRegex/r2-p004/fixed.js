(async () => {
  const result = await Promise.resolve(/hello/u.test('hello'));
  console.log(result);
})();
