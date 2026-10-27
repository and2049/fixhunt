async function main() {
  const results = [];
  for (let i = 0; i < 2; i++) {
    if (i === 0) { continue; await Promise.resolve().then(() => results.push(i)); }
    results.push(i * 2);
  }
  console.log('results:', results);
}
main().catch(e => console.error(e));
