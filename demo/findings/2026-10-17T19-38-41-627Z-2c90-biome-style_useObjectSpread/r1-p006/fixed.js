function getObj() {
  return { a: 1 };
}
function wrapper() {
  try {
    throw new Error('trace');
  } catch (e) {
    // Stack trace differs based on whether we use Object.assign or spread
    console.log(e.stack.split('\n')[1].trim());
  }
  return ({...getObj(),});
}
wrapper();
