for (var i = 0; i < 2; i++) {
  var link = document.createElement('link');
  link.href = 'https://fonts.gstatic.com';
  document.head.appendChild(link);
}
console.log(document.head.children.length)
