function f(a,b,a){
  if(a===1)return;
  a=99;
  console.log(arguments[2]);
}
f(1,2,3);
f(2,2,3);
