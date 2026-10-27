let callCount = 0;
const obj = {
  get value() {
    callCount++;
    if (callCount > 2) throw new Error('Too many calls');
    return callCount === 1;
  }
};
try {
  console.log('First !!:', !!obj.value, 'calls:', callCount);
  console.log('Second !!:', !!obj.value, 'calls:', callCount);
  console.log('Third !!:', !!obj.value, 'calls:', callCount);
} catch(e) {
  console.log(e.name + ': ' + e.message);
}
// Fix to obj.value would show same call count progression — proving timing unchanged
