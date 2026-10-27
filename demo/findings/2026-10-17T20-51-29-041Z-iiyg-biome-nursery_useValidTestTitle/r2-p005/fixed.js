['   ', '\t\n\r  '].forEach(title => {
  const len = title.length;
  test(title, () => {
    console.log(len === 0 ? 'zero' : len > 0 && len <= 2 ? 'short' : 'long');
  });
});
