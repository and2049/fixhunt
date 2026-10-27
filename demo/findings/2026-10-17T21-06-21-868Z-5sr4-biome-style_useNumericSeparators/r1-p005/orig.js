try { 
  eval('obj.12345');
} catch(e) {
  console.log(e.name + ': ' + e.message);
}
console.log((12345).toString());
