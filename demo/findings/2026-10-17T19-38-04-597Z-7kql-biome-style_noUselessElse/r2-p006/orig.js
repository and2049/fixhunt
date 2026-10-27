let log = '';
try {
  if (true) {
    return;
  } else {
    log += 'else'; // moved after try, never runs
  }
} finally {
  log += 'finally';
}
console.log(log || 'empty');
