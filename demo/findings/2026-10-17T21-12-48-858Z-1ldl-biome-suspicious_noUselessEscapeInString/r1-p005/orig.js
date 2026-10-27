function tag(strings) {
  return strings.raw[0].length;
}
console.log(tag`hello\aworld`);
