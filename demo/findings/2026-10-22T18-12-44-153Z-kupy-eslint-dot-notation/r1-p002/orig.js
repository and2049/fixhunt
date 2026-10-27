let obj = {123: 'value'}; try { let v = obj[\'123\']; console.log('got:', v); } catch(e) { console.log('err:', e.name); } try { eval('obj.123'); } catch(e) { console.log('fix err:', e.name); }
