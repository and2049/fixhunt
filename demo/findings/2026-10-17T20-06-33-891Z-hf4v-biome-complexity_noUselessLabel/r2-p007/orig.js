console.log(typeof f); // should be 'function' if hoisted
label: function f() { return 42; }
console.log(f());
