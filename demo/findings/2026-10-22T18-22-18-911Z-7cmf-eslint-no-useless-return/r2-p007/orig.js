async function f() {
  console.log('async start');
  return;
}
f().then(v => console.log('resolved with:', v)); // undefined
// If return; removed, still resolves to undefined
// But if someone expects early exit semantics, confusion
