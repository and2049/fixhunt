const obj = {
  get val() {
    print('getter called');
    return 42;
  },
  set val(v) {
    print('setter called with: ' + v);
  }
};

Object.defineProperty(obj, 'side', {
  get: function() {
    print('Object.defineProperty getter called');
    return 1;
  },
  enumerable: true
});

if (true) {
  const v = obj.val; // original: getter called inside if
} else {
  const v = obj.val; // moved before if in the fix
}
print('done');
