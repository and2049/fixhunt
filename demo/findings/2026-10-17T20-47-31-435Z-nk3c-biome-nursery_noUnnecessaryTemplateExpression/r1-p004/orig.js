// This tests near-miss: comment inside interpolation - rule should NOT trigger
const msg = `${'hello' /* ignored */}${'world'`;
console.log('Message:', msg);
