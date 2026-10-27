outer:
for (let i = 0; i < 3; i++) {
  if (Math.random() < 0.5) {
    break outer; // original: break exits the labeled loop from inside else
  } else {
    innerBreak: break outer; // labeled break inside else
  }
}
print('loop finished, counter should be 3');
print('i value: ' + i);
print('if i===3 label visibility preserved');
