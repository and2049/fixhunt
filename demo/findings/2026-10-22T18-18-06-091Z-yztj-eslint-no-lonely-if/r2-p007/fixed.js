async function fn() {
  if (false) {
    return 1;
  } else if (true) {
      await Promise.resolve(2);
      return 3;
    }
}
fn().then(v => console.log('result:', v));
