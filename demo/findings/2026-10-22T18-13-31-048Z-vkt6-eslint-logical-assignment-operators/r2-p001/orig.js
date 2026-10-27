// comment before
let x = 0;
// x = x /* mid */ || 1; // after
x = x /* LHS comment */ || /* RHS comment */ 1;
console.log(x);
