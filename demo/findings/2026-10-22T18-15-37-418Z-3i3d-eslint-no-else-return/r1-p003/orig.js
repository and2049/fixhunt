function checkEmpty(a) {
  try {
    if (a < 0) { throw 'neg'; }
    else {}                    // Hazard: empty else
    return 'ok' + a;
  } catch (e) {
    return 'bad' + typeof e;
  }
}
console.log(checkEmpty(-1));
console.log(checkEmpty(5));
