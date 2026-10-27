'use strict';
(function() {
  var data = [[1], [2], [3]];
  try {
    delete data[0];
    const result = data.map(x => x).flat();
    console.log(result.length);
  } catch (e) { console.log(e.name); }
})();

(function() {
  'use sloppy';
  var data2 = [[1], [2], [3]];
  delete data2[0];
  const result = data2.map(x => x).flat();
  console.log(result.length);
})();
