switch(0) {
  case 0:
    function create() {
      const l = document.createElement('link');
      l.href = 'https://fonts.gstatic.com';
      return l;
    }
    break;
}
const links = [create(), create()];
links.forEach((l, i) => {
  if (!l.hasAttribute('rel')) l.setAttribute('rel', 'preconnect');
  console.log(i, l.getAttribute('rel'));
});
