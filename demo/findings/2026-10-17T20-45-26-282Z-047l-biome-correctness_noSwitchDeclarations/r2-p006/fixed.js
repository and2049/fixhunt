function test(){
  switch(0){case 0: {
    const x = [1,2]
    [x[0], x[1]] = [x[1], x[0]]
    return x[0] + ',' + x[1]}
  }
}
console.log(test());
