let x = 0;
const log = v => { console.log('log:', v); return ++x; };
expr = (log(1), "ab", log(2));
console.log('Result:', expr);
