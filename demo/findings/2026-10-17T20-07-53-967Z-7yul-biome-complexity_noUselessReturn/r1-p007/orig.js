let val=0,log=[];
const o={set v(x){log.push('set '+x);val=x}};
function f(x){
  if(x===undefined)return;
  o.v=x;
}
f(1);
f();
