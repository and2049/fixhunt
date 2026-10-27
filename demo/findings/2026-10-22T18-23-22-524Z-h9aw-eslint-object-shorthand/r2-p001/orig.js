function f() {
  try {
    return {a: a}; // triggers rule
  } catch (e) {
    return e.name + ': ' + e.message;
  }
}
console.log(f());
