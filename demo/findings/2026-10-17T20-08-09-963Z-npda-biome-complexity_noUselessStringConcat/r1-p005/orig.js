// Hazard 5: Exception in concatenation subexpression
function risky() { throw new Error('fail'); }
try {
  const result = \"before\" + risky() + \"after\";
} catch (e) {
  console.log(e.constructor.name + ': ' + e.message);
}
