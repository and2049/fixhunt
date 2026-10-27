let obj = {
  toString: () => '   abc   '
};
console.log((obj).trimLeft() + 'def');
