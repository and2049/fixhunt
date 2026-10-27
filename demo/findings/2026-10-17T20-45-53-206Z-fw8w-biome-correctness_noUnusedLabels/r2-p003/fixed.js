for (let i = 0; i < 3; i++) {
  if (i === 1) eval('break LOOP;');
  console.log(i);
}
console.log('after loop');
