let exportedValue = 99;
label: { /* dummy label */ }
try {
  eval('console.log(label)'); // attempts to reference label
} catch (e) {
  console.log(e.name);
}
console.log(exportedValue);
