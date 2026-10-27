try {
  outer: {
    try {
      throw new Error('break outer');
    } catch (e) {
      if (e.message === 'break outer') break outer;
      throw e;
    }
    console.log('not reached');
  }
} catch (e) {
  console.log('caught:', e.message);
}
console.log('done');
