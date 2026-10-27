function f() {
  try {
    return {a}; // triggers rule
  } catch (e) {
    return e.name + ': ' + e.message;
  }
}
console.log(f());
