let a = 1;
// This comment is on the line with the shorthand candidate
const obj = {/* keep me */ a: a, b: 2};
// After fix: {/* keep me */ a, b: 2} — comment preserved? Autofix may keep it.
// But if it deletes the whole prop, comment goes.
// We test by having comment on the prop being removed.
console.log(obj.a);
