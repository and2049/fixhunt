(function () {
  var globalInEval = 100;
  eval('var localInEval = 200; console.log(typeof globalInEval, typeof localInEval);');
  try {
    console.log(typeof globalInEval, typeof localInEval); // localInEval leaked if var
  } catch (e) {
    console.log(e.name + ': ' + e.message);
  }
})()
