function logValue(flag) {
  const out = [];
  if (flag) {                  // Enter condition
    return 42;                 // Magic number
  } /* ignore */               // Comment on brace
                              // Brace with potential comment loss
    /* preserved */            // This should survive
    out.push('hi');
  
  out.push(flag ? 't' : 'f');
  return out.join('|');
}
console.log(logValue(true));
console.log(logValue(false));
