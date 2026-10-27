let count = 0;
function side() { return ++count; }
console.log((/a {2}b/.test('a  b'), side()) + (side(), /x {4}y/.test('x    y')));
