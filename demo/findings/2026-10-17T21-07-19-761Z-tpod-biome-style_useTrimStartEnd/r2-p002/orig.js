let side = 0;
function log() { return ++side; }
const result = log() && '  hello'.trimLeft();
console.log(`side=${side}, result='${result}'`);
