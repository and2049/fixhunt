function test(){
  switch(0){case 0: {
    const obj = { a: null }
    return obj.a?.b ?? 'default'}
  }
}
console.log(test());
