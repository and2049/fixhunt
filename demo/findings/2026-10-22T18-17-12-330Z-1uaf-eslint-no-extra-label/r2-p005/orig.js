let v = 5;
C: { with ({v: 10}) { break C; } }
console.log(v);
