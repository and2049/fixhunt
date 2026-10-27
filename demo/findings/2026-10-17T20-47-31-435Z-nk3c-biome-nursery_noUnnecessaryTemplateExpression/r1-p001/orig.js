let x = 0;
const log = v => { console.log('log:', v); return ++x; };
expr = (log(1), `${'a'}${'b'}`, log(2));
console.log('Result:', expr);
