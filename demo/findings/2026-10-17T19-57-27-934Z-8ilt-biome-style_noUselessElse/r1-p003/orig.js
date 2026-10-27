let result = '';
loop: {
  if (true) { break loop; }
  else { result += 'b'; }
}
result += 'a';
console.log(result);
