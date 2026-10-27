const obj = {
  get link() {
    const l = document.createElement('link');
    l.href = 'https://fonts.gstatic.com';
    return l;
  }
};
const f = obj.link;
try { console.log(f.getAttribute('href')); } catch(e) { console.log(e.name); }
const bound = obj.link.bind(obj);
bound().setAttribute('rel', 'preconnect');
console.log(bound().getAttribute('rel'));
