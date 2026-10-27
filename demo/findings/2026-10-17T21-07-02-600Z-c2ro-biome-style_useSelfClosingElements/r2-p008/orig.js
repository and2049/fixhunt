let log = '';
function getValue() { log += 'called'; return 42; }
const el = <div data={getValue()}></div>;
console.log(log);
