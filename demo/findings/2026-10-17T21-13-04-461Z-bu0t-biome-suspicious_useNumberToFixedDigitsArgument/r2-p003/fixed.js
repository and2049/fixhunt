const obj = {
  toFixed: () => {
    if (arguments.length > 0) throw new Error('no args expected');
    return 'custom';
  }
};
try {
  console.log(obj.toFixed());
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
