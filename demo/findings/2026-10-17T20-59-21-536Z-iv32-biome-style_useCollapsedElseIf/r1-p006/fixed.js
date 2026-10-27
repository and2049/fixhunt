let v;
if (false) {} else if (true) {
    function inner() { return 42; }
    v = inner();
  }
console.log(typeof v === 'number' ? v : 'undefined'); // Should be undefined in ES2015+ due to TDZ-like block scoping
