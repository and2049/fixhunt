let log = '';
outer: for (let i = 0; i < 2; i++) {
  try {
    if (i === 0) continue outer;
    let x = i;
    let y = !!x; // triggers rule only when i=1 (x=1 -> y=true)
    log += 'y:' + y + '|';
  } finally {
    log += 'f';
  }
}
console.log(log);
// Expected: for i=0: continue -> skip body, finally runs -> log+='f'
//           for i=1: y=true -> log+='y:true|', finally -> +'f' -> total 'fy:true|f'
// If rule rewrites y = x ? true : false to y = x, then for i=1: y=1 -> log+='y:1|'
// Output would be 'fy:1|f' -> different}
