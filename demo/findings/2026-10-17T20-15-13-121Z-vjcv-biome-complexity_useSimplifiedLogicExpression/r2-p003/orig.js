let a = 0;
false || (a = 1);
console.log(a); // should remain 0 if short-circuited
