// Hazard 4
async function main() {
  const dir = await Promise.resolve(__dirname);
  console.log(dir.length);
}
main();
