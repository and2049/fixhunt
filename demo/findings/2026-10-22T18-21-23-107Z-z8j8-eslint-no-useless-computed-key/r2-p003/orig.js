for (let i = 0; i < 2; i++) {
  ({[i]: v} = [{}, {v: 1}]);
  console.log(v?.v ?? 0);
  var v = 99;
}
