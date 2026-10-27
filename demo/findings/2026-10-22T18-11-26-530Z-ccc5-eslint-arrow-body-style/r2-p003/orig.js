try {
  const x = () => { throw new Error('test'); };
  x();
} catch (e) {
  console.log(e.message);
}
