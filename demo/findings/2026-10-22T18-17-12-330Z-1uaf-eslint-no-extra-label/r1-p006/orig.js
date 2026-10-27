label: {
  const code = 'break label;';
  try { eval(code); } catch (e) {
    console.log(e.name + ': ' + e.message);
  }
}
