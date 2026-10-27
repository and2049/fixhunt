const o = {
  ["2"]: "two",
  ["1"]: "one"
};
let s = '';
for (const k in o) s += k;
console.log(s); // expects '21' if computed, '12' if literal due to numeric key ordering
