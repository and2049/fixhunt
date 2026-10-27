let obj = {__proto__: {toString(){return 'proto'}}};
let copy = {...obj, a: undefined}; // rule triggers on 'a: undefined'

let log = [];
log.push(String(copy.a));
log.push(String(copy.toString()));
log.push(String(Object.getPrototypeOf(copy)));

// Re-assign after use
data = {x:1};
copy = {...data, y: undefined}; // another trigger
log.push(String(copy.y));

console.log(log.join(' | '));
