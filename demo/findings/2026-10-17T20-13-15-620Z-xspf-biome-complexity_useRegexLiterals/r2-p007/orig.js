{
  function getFlags() { return 'g'; }
  try {
    console.log(new RegExp('a', getFlags()).test('a'));
  } catch (e) {
    console.log(e.constructor.name + ': ' + e.message);
  }
}
