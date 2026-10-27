function test() {
  try {
    throw {msg: 'error', code: 42};
  } catch (code, msg) {
    console.log(`msg=${msg}, code=${code}`);
  }
}
test();
