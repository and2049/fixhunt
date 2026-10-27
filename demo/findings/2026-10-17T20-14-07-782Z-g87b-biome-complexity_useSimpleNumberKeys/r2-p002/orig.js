
const obj = { \u{41}: /a/g };
obj[\u{41}].lastIndex = 0;
console.log(obj[\u{41}].test('a'), obj[\u{41}].lastIndex);
