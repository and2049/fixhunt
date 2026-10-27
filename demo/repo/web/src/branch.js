export function label(n) {
  let text = "none";
  if (n > 0) {
    return "positive";
  } else {
    let text = "non-positive";
    return text;
  }
}
