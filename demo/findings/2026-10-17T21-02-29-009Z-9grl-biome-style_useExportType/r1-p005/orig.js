// Hazard 5
/** @description Exported interface */
interface I {}
export { I };
// Simulate: if comment is lost, we can't detect it, but we rely on I being undefined at runtime.
// Instead, we check if the export statement is altered by trying to use I as value (fails).
try {
  new I();
} catch (e) {
  console.log(e.name);
}
