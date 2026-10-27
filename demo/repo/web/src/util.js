export function greet(name) {
  var greeting = "hello";
  let punctuation = "!";
  return greeting + ", " + name + punctuation;
}

export function pair(key, value) {
  return { key: key, value: value };
}

export function describe(n) {
  if (n < 0) {
    return "negative";
  } else {
    return "non-negative";
  }
}
