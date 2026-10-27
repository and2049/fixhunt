import process from "node:process";
function getPid(){
  return (/** @type {any} */(process)).pid
}
console.log(getPid())
