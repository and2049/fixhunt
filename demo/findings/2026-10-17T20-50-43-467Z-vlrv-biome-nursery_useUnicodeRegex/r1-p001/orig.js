outer: {
  let result = '';
  try {
    for (let i = 0; i < 2; i++) {
      const m = /a/.exec('a');
      result += m ? m[0] : 'x';
      if (i === 0) break outer;
    }
  } finally {
    result += 'f';
  }
  console.log(result);
}
