(() => {
  console.log(typeof x); // TDZ: ReferenceError if let x not yet initialized
  let x = 0;
  let y = !!x; // triggers rule
  console.log('y:', y);
})();
