let trace = '';
const step = (label) => {
  trace += label;
  return label.charCodeAt(0);
};

// Comma return - rule triggers here
const seq = () => (step('A'), step('B'));

const val = seq();
console.log('trace:', trace);
console.log('value:', val);
