let x = { a: 1 };
const y = { b: 2 };
// Expected trigger: true? No - because arg is not {}, so expect_trigger=false
const ref = Object.assign(x, y);
x.a = 99;
console.log(ref.a);
