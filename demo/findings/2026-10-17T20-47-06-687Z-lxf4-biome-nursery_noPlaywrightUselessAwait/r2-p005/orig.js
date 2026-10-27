outer: {
  try {
    await/* mark */ page.locator('.test');
    break outer;
  } finally {
    console.log('finally ran');
  }
}
console.log('after');
