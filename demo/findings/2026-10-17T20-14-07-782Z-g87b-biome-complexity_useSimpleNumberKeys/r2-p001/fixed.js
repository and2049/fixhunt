"use strict";
const obj = { 0o755: 'allowed' };
try {
  // Simulate old env check: throw if octal detected via string conversion quirk
  const str = String(0o755);
  if (/^0[0-7]+$/.test(str)) throw new Error('Old engine: octal literal treated specially');
  console.log(obj[0o755]);
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
