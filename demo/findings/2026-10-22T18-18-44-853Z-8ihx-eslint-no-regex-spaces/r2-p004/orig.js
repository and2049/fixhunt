let count = 0;
function side() { return ++count; }
console.log((/a  b/.test('a  b'), side()) + (side(), /x    y/.test('x    y')));
