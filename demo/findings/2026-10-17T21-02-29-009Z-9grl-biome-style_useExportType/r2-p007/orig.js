const N = { prop: 'x' };
export { N };
// Biome fix: export { type N }; -> invalid
console.log(N.prop); // Should print 'x'
