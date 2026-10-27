function str(parts) {
  return parts.raw[0] + '|' + parts.raw[1];
}
console.log(str`a${12345}b`);
