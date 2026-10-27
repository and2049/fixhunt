let result = '';
for (let i = 0; i < 2; i++) {
  switch(i) {
    case 0:
      function f() { return 'a\251b'; }
      result += f();
      break;
    case 1:
      result += f(); // reuse function from case 0
      break;
  }
}
console.log(result);
