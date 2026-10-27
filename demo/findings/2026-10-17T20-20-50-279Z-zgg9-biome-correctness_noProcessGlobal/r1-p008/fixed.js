import process from "node:process";
try{
  console.log(typeof process)
}catch(e){
  console.log(e.name, e.message)
}
