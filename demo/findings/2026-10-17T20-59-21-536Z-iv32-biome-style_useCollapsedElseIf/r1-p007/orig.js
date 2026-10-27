let u = 1;
for (let i = 0; i < 2; i++) {
  if (i === 0) {} else {
    if (true) {
      let u = i + 10;
      console.log(u); // Should log 11 only once (i=1)
    }
  }
}
