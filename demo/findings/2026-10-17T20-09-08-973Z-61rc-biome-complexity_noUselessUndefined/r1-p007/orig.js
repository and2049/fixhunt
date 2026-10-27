let trace = [];
outer: for(let i=0; i<2; i++){
  try{
    if(i===0){
      trace.push('a');
      break outer;
    }
    trace.push('b');
    return undefined; // rule triggers
  } finally{
    trace.push('finally');
  }
}

function inner(){ 
  trace.push('inner start');
  if(true) yield undefined; // rule triggers
  trace.push('inner end');
}

for(const v of inner()){ trace.push('yielded: '+v); }

console.log(trace.join(' | '));
