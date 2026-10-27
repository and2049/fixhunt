outer: {
  try {
    if (true) break outer;
    console.log('unreachable');
  } finally {
    console.log('finally ran');
  }
}
console.log('done' + (() => { break outer; })());
