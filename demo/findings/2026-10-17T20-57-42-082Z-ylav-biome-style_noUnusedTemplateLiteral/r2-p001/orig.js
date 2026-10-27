const pattern = 'hello\\u{1F600}world'; // u-flag needs raw \u{...}
const regexStr = `\\${pattern}`; // Template: raw backslashes preserved
try {
  const r = new RegExp(regexStr, 'gu');
  console.log(r.test('hello😀world'));
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
