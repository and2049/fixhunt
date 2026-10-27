'use strict';
(function() {
  var data = [[1], [2], [3]];
  try {
    delete data[0];
    const result = data.flatMap(x => x);
    console.log(result.length);
  } catch (e) { console.log(e.name); }
})();

(function() {
  'use sloppy';
  var data2 = [[1], [2], [3]];
  delete data2[0];
  const result = data2.flatMap(x => x);
  console.log(result.length);
})();
