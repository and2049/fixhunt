outer:
for (let outer = 0; outer < 2; outer++) {
  inner:
  for (let inner = 0; inner < 2; inner++) {
    if (inner === 1) break outer;
    console.log('inner', inner);
  }
  console.log('outer', outer);
}
