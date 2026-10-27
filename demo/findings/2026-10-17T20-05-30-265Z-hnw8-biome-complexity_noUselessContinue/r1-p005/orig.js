for (let i = 0; i < 2; i++) {
  if (i === 0) { continue; }
  function inner() { return i; }
  console.log('inner:', inner());
}
