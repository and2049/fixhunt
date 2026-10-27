let x = undefined;
try {
  console.log(`Result: ${  x}`);
} catch (e) {
  console.log(`Caught: ${  e.name  }: ${  e.message}`);
}
