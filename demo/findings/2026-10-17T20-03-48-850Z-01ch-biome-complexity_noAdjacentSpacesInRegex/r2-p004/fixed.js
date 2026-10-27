{
  function check(s) { return /test {2}case/.test(s); }
  console.log(check('test  case'));
  console.log(check('testcase'));
}
