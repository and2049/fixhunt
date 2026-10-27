let finallyRan = false;
try {
  if (false) { return 'skipped'; }
  else { return 'not skipped'; }
} finally {
  finallyRan = true;
}
console.log('finally ran:', finallyRan);
