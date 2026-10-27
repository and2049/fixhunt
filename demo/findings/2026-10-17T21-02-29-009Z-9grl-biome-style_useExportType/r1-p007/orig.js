// Hazard 7
let X = 1;
{ export { type X }; } // block scope
if (typeof X === 'number') {
  console.log('value');
} else {
  console.log('type');
}
