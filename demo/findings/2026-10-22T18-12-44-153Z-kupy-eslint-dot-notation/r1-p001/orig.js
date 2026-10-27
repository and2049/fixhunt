let obj = {'a-b': 42}; try { let result = obj[\'a-b\']; console.log('got:', result); } catch(e) { console.log('catch1:', e.name); } try { // This line will be fixed by dot-notation rule but is invalid syntax
  eval('obj.a-b');
} catch(e) { console.log('catch2:', e.name); }
