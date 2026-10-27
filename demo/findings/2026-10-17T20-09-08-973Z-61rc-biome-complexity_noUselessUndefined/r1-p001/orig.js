let log = [];
function capture(v){ log.push(v); }

// Hazardous pattern: default in destructuring
data = {a: null}; // note: value is null, not missing
try {
  const {a = undefined} = data;
  capture('got ' + String(a));
} catch(e) {
  capture(e.name + ': ' + e.message);
}

console.log(log.join(' | '));
