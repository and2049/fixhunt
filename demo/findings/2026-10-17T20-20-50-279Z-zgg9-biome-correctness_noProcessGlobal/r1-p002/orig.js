function outer(){
  let process = 'local'
  if(true){
    console.log(typeof process)
    return process
  }
}
outer()
