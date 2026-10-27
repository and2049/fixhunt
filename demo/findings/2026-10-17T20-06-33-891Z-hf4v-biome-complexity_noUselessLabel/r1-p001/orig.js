function f(a = 1, ...args) {
  lbl: for (let i = 0; i < args.length; i++) {
    console.log('arg:', args[i], 'length:', arguments.length);
    if (i === 0) break lbl;
  }
}
f(5, 6, 7);
