function test(){
  let arr = new Array(3);
  switch(0){case 0:
    const v = arr[1] = 99
  }
  return arr[1];
}
console.log(test());
