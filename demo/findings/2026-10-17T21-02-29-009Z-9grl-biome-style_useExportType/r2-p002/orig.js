// @ts-nocheck
const S = 'hello';
export { S };
console.log(S.toUpperCase());
// Biome fix: export { type S }; -> SyntaxError in JS
