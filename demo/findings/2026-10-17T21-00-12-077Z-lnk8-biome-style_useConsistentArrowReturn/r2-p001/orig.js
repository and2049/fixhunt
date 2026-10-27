const Target = class {
  constructor(x) { this.value = x; }
};
let madeViaNew = null;
try {
  madeViaNew = new Target(1);
} catch (_) {}
console.log('madeViaNew:', madeViaNew ? madeViaNew.value : 'none');

// Arrow function returning class - rule triggers here
const makeTarget = (cls) => { return cls; };
let madeViaConstruct = null;
try {
  // Simulate incorrect construction attempt using Reflect.construct
  madeViaConstruct = Reflect.construct(makeTarget([Target]), []);
} catch (e) {
  console.error(e.name + ': ' + e.message);
}
if (madeViaConstruct && madeViaConstruct.value !== undefined) {
  console.log('madeViaConstruct.value:', madeViaConstruct.value);
} else if (madeViaConstruct instanceof Target) {
  console.log('madeViaConstruct is instance:', madeViaConstruct.value);
} else {
  console.log('madeViaConstruct:', madeViaConstruct);
}
