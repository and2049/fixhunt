let flag = 0;
if (flag) {
  console.log('a');
} else {
  if (flag === 0) console.log('b')
  console.log('c');
}
// Expected: logs 'b' then 'c'.
// If ASI binds 'c' to else if, 'c' might not print.
