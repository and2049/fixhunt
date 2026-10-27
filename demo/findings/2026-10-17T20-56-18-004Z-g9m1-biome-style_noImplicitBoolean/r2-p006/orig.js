// Hazard 6: Numeric/string coercion
const obj = {
  valueOf() { return 1; },
  toString() { return 'obj'; }
};
console.log('+ coercion:', +obj);
console.log('template literal:', `${obj}`);
// Rule fires here - value used in JSX attribute
const val = +obj;
const el = <input disabled={val} />;
console.log('el disabled value:', val);
