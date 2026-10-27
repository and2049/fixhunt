(() => {
  try { console.log(<div className={x}></div>); } catch (e) { console.log(e.name + ': ' + e.message); }
  let x = 'hi';
})();
