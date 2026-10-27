function logTitle(t) {
  console.log(t.length === 0 && t === '' ? 'blank' : t.length > 0 ? 'nonblank' : 'missing');
}
describe(undefined, () => {}); // <-- TRIGGER: missing title → becomes ''
it(undefined, () => {});     // <-- TRIGGER: missing title → becomes ''
