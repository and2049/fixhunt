try {
  const re = /fail  here/;
  throw new Error('deliberate');
} catch (e) {
  console.log('Caught:', e.constructor.name, e.message);
}
