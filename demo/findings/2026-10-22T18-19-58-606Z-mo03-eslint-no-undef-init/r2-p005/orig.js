async function main() {
  var p = undefined;
  console.log('start:', p);
  p = Promise.resolve(42);
  console.log('awaited:', await p);
}
main().catch(e => console.log(e));
