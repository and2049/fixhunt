const obj = {
  valueOf() { return 42; },
  toString() { return 'hello'; }
};
const str = `${obj}`;
const num = +obj;
const el = <div data-val={str} data-num={num}></div>;
console.log(el.props['data-val'] + el.props['data-num']);
