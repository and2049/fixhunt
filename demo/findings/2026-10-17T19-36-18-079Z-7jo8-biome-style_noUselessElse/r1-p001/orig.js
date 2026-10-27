let counter = 0; const sideEffect = () => { counter++; return counter; };

if (Math.random() < 0.5) {
  sideEffect(); // original order: else block runs after sideEffect call
} else {
  sideEffect(); // moved before the if in the fix
}

print('counter after if-else: ' + counter);
print('expected counter >= 2, got: ' + counter);
