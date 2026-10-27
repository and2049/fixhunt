outer: for (;;) { inner: { if (true) break outer; } ({'a': x} = {a: 1}); console.log(x); break; }
