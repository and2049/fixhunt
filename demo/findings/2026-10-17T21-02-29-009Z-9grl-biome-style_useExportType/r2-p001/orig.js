const V = 1;
export { V };
try {
  console.log(V);
} catch (e) {
  // This won't run initially
}
// Biome will attempt to fix to: export { type V }; which is invalid
