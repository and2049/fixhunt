outer: {
  let result = '';
  inner: {
    if (/=a/.test('xa')) {
      break outer;
    }
    result += 'not broken';
  }
  result += ' after inner';
}
console.log(result);
