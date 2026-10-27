// Hazard 4
async function main() {
  const dir = await Promise.resolve(import.meta.dirname);
  console.log(dir.length);
}
main();
