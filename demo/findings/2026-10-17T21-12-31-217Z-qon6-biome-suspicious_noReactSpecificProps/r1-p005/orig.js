for (var i = 0; i < 2; i++) {
  var className = i === 0 ? 'first' : 'second';
  console.log(<div className={className}></div>);
}
