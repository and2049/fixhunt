const proto = { __proto__: null, toString: () => 'hidden' };
function makeObj() {
  switch(true) {
    case true:
      const desc = Object.getOwnPropertyDescriptor(proto, '__proto__');
      return () => desc.get.call({});
  }
}
try {
  const fn = makeObj();
  console.log(fn());
} catch(e) {
  console.log(e.name);
}
