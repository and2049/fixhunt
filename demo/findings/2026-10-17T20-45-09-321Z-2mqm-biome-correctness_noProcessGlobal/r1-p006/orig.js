if (true) {
  console.log(process.version); // expects global
  let process = { version: 'local' };
  console.log(process.version);
}
