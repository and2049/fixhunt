const protoObj = { __proto__: null };
const key = `${'__proto__'}${'sub'}`;
try {
  protoObj[key] = 'should not set proto';
  console.log('Assignment succeeded, proto unchanged:', protoObj.__proto__ === null);
} catch (e) {
  console.log('Error:', e.name, e.message);
}
