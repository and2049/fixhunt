try { 
  eval('obj.12345');
} catch(e) {
  console.log(e.name + ': ' + e.message);
}
console.log((12_345).toString());
