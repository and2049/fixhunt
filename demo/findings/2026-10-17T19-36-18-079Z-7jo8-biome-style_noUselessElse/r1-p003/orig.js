try {
  if (true) {
    const x = 1;
    print('x in if: ' + x);
  } else {
    const x = 2; // original: x declared inside else
  }
  print('x after block: ' + x); // ReferenceError if TDZ fires
} catch (e) {
  print('Caught: ' + e.constructor.name + ': ' + e.message);
}
print('end');
