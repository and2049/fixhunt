import process from "node:process";
let log = '';
try { process = { log: v => (log += v) }; } catch (e) { log += 'catch:' + e.name; }
process.log('ok');
console.log(log);
