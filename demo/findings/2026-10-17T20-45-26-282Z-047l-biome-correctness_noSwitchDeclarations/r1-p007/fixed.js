let out = '';
lab: {
  switch(1) {
    case 1: {
      const msg = 'A';
      break lab;
    }
  }
  out += 'B';
}
console.log(out);
