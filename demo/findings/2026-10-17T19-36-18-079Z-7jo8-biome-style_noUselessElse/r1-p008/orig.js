let depth = 0;
try {
  outer:
  for (let i = 0; i < 2; i++) {
    if (true) {
      depth++;
      if (Math.random() < 0.5) {
        break outer; // original break from inside nested else
      } else {
        depth++;
        continue outer; // original continue from inside else
      }
    }
  }
  print('depth: ' + depth);
  print('loop terminated normally');
} catch (e) {
  print('Caught: ' + e.constructor.name);
}
print('finally block simulated');
