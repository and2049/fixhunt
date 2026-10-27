{
  function f() { return { toFixed: () => 'orig' }; }
  console.log(f().toFixed());
  {
    function f() { return { toFixed: n => `${n || 0}-fixed` }; }
    console.log(f().toFixed());
  }
}
