function f() {
  if (true) return [,1];
  
    return [2,];
}
console.log(JSON.stringify(f()));
