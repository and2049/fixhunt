try {
  throw { message: 'test' };
} catch (process) {
  console.log('caught:', process.message);
}
console.log('after catch');
