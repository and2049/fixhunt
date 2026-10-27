// Hazard 4: RegExp lastIndex with g flag
const regex = /a/g;
console.log('first match:', regex.exec('baaab'));
console.log('lastIndex after first:', regex.lastIndex);
// Rule fires here - if fixed, may re-evaluate regex in JSX
const el = <input disabled={!!regex.exec('baaab')[0]} />;
console.log('lastIndex after JSX:', regex.lastIndex);
