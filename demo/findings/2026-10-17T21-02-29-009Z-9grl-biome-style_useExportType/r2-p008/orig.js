const P = {}
P.__proto__ = { x: 1 };
console.log(P.x); // 1
class Q {}
export { P, Q }; // Rule silent on P (used via __proto__), Q (constructor)
// No fix applied, behavior preserved
