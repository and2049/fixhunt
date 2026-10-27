{
  function f() { return '  ok  '; }
  const result = f().trimEnd();
  console.log(`'${result}'`);
}
