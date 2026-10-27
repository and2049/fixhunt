let tmp;
try {
  if (true) {
    // no declaration
  } else {
    tmp = 1; // original: assignment inside else
  }
  print('tmp after: ' + tmp);
  // Simulate hoisting: tmp is now in scope before the if
  if (tmp === undefined) {
    tmp = 2; // this line sees tmp in TDZ if hoisted weirdly
  }
} catch (e) {
  print('Caught: ' + e.constructor.name + ': ' + e.message);
}
print('end');
