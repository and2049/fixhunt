outer: {
  try {
    (function() {
      if (true) break outer;
      console.log('unreachable');
    })();
    console.log('after break');
  } finally {
    console.log('finally');
  }
}
