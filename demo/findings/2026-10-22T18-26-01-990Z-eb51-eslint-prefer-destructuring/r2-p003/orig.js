// Hazard 3: Near-miss - not flagged, so fix should not apply
let obj = { a: 1 };
if (true) (obj.a = 2); // AssignmentExpression, not VariableDeclarator
console.log(obj.a);
