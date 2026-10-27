function process(arr) {
  let total = 0;
  arr.forEach((v, i) => {
    switch(i) {
      case 0: {
        const captured = v + 10;
        return total += captured;
      }
      default: {
        const fallback = v || -1;
        return total -= fallback * 2;
      }
    }
  });
  console.log('Result:', total);
}
process([5]); // hole at index 1
