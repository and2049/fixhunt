function test(){
  let log = [];
  switch(0){case 0:
    const obj = { get x(){ log.push(1); return 2 } }
    log.push(obj.x);
    return log;
  }
}
console.log(test());
