let result = '';
loop: {
  if (true) { break loop; }
  result += 'b'; 
}
result += 'a';
console.log(result);
