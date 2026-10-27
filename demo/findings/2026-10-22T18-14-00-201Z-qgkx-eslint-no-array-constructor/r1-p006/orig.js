(function(){
  const iframe = document.createElement('iframe');
  document.body.appendChild(iframe);
  const Arr = iframe.contentWindow.Array;
  const a = Arr(3);
  console.log(a instanceof Arr);
  const b = [...[]]; // trigger fix elsewhere
  console.log(a instanceof Array);
})();
