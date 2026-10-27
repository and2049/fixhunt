try {
  const re = /fail {2}here/;
  throw new Error('deliberate');
} catch (e) {
  console.log('Caught:', e.constructor.name, e.message);
}
