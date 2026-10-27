// Parse string values with a caller-supplied converter for the non-integer part.
export function parseAll(values, Number) {
  return values.map((v) => parseInt(v, 10) + Number(v));
}
