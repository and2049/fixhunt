function outer(){
  switch(0){case 0:
    function inner(){ return 'inner' }
  }
  try{ return inner() }catch(e){ return e.message }
}
console.log(outer());
