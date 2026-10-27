function* gen(){
  yield undefined; // triggers rule
  yield;         // equivalent, no trigger
}

const it = gen();
let log = [];
log.push(JSON.stringify(it.next()));
log.push(JSON.stringify(it.next()));
log.push(JSON.stringify(it.next()));

console.log(log.join(' | '));
