function test(){
  let y = 'outer';
  switch(0){case 0: {
    const y = 'inner';
    return y;}
  }
}
console.log(test());
