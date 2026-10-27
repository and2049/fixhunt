{  // Block scope
  let x = 1;
  // Arrow in block - rule triggers
  const inc = () => x + 1;
  x = inc();
  console.log('block x:', x);
}

switch(1) {
  case 1:
    let y = 2;
    // Arrow in case - rule triggers
    const double = (z) => z * 2;
    y = double(y);
    console.log('case y:', y);
    break;
}

label: {
  let z = 3;
  // Arrow in labeled block
  const addTen = () => z + 10;
  z = addTen();
  console.log('labeled z:', z);
  break label;
}
