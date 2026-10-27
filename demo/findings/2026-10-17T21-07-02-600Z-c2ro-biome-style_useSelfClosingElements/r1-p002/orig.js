const el = document.createElement('div');
el.innerHTML = '<div></div><span>';// rely on parsing
console.log(el.childElementCount);
