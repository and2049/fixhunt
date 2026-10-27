function f(){
  for(var i=0;i<2;i++){
    if(i===0)return;
    console.log(i);
    var i=100;
  }
}
f();
