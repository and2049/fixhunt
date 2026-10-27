outer: {
  try {
    (function() {
      if (true) break outer;
      return 1;
    })();
    console.log('unreachable');
  } finally {
    console.log('finally');
  }
}
console.log('after');
