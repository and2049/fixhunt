if (true) {
  if (false) {
    console.log(x); // TDZ if let x were here, but it's not
  }
  let x = 1;
}
console.log('x after:', typeof x === 'undefined' ? 'undefined' : x);
