function test(title, handler) {
  try {
    handler(title);
  } catch (e) {
    console.log('caught:', e.message);
  }
}
function bad() {
  throw new Error('boom');
}
test(bad(), msg => { console.log('handler:', msg); });
