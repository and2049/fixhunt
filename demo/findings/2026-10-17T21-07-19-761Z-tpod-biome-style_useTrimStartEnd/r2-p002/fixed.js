let side = 0;
function log() { return ++side; }
const result = log() && '  hello'.trimStart();
console.log(`side=${side}, result='${result}'`);
