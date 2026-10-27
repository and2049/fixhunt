function f(x,y=x+1){
  if(x===undefined)return;
  console.log(x,y,arguments.length,arguments[1]);
}
f(5);
f();
