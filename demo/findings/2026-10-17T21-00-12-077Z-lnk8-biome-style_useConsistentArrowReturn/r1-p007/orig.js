const makeClass = () => {
  return class {
    constructor() { this.x = 1; }
  };
};
const C = makeClass();
const c = new C();
console.log(c.x);
