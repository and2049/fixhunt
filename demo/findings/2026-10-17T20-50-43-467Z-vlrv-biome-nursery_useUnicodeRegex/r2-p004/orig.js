(async () => {
  const result = await Promise.resolve(/hello/.test('hello'));
  console.log(result);
})();
