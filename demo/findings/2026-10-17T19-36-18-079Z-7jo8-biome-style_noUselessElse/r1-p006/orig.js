{
  if (Math.random() < 0.5) {
    function bar() { return 1; }
    print('bar called: ' + bar());
  } else {
    function bar() { return 2; } // original: function declaration inside else
    print('else bar called: ' + bar());
  }
  // In the fix, bar is hoisted to enclosing scope, last declaration wins
  print('final bar: ' + bar());
}
print('end');
