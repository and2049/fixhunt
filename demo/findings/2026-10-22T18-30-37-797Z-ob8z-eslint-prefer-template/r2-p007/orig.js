let used = 0;
0, used = ('x' + 'y'), console.log(used); // Sequence: assigns then logs
// Rule does not fire on 'x'+'y' here because it's inside sequence? Actually it should.
// But we want near-miss: make it so rule doesn't fire due to context.
// Let's try: if the '+' is in a sequence but the whole thing is ignored...
0, ('ignored' + 'text'); // This should trigger rule but result ignored
console.log('side effect only if assignment');
