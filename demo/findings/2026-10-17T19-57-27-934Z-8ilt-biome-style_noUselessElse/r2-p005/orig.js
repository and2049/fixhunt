let i = 0;
if (false) { i++ }
else {
  console.log(i); // should print 0
  i++;
}
console.log(i); // should print 1 if not lifted, 2 if lifted before log
