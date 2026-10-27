let threw = false;
let errorMsg = '';

// Arrow function that throws - rule triggers
const risky = () => { throw new Error('fail'); };

try {
  risky();
} catch (e) {
  threw = true;
  errorMsg = e.name + ': ' + e.message;
}
console.log('threw:', threw);
console.log('error:', errorMsg);
