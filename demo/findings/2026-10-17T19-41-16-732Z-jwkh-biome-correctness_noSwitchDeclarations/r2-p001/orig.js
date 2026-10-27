function f(){
  var x = 1;
  switch(0){case 0: let y = 2; with({x:y}) console.log(x); break;}
}
