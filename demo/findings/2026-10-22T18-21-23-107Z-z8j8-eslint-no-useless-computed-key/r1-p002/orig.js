try { ({0: x} = {0: 42}); console.log(x); } catch (e) { console.log(e.name + ': ' + e.message); }
