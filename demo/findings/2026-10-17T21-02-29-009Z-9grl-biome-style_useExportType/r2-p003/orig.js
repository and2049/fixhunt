if (false) {
  const B = 2;
  export { B }; // Invalid in original, flagged but fix irrelevant
}
console.log('no crash');
