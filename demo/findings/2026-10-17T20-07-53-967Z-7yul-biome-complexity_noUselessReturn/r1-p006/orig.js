let obj={valueOf:()=>{console.log('v');return 42},toString:()=>{console.log('t');return '4'}};
function f(x){
  if(x===obj)return;
  console.log(+x);
}
f(obj);
