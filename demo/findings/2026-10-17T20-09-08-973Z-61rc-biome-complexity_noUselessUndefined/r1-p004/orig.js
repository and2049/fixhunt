let out = [];
{ 
  function h(){ out.push('block'); }
  if(true){ function h(){ out.push('redeclared'); } }
  h();
}

switch(0){
  case 0:
    function h(){ out.push('case'); }
    break;
}

h();

label: {
  function h(){ out.push('label'); }
  break label;
}

h();

console.log(out.join(' | '));
