outer:
for (let i = 0;;) {
  let counter ;
  if (i === 0) break outer;
  counter = 1;
  i++;
}
console.log(typeof counter); // ReferenceError if fix removes declaration
