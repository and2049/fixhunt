const allowed = ['trusted.com'];
const url = 'https://trusted.com/path';
if (allowed.some(d => url.includes(d))) {
  console.log('Allowed domain, no fix needed');
} else {
  console.log('Fix would apply');
}
