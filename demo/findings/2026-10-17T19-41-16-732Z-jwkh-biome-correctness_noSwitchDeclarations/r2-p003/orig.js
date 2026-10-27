function f(){
  const obj = {valueOf:()=>5,toString:()=>'5'};
  switch(obj){case 5: let y = +obj + ''; console.log(y); break;}
}
