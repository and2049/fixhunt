// @ts-ignore
// This simulates TS ambient context via comment-triggered rewrite risk
/* declare */ var globalValue = 123;
console.log(typeof globalValue === 'number' ? globalValue : 'invalid');
