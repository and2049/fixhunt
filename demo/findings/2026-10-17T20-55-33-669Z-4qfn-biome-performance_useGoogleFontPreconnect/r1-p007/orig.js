const proto = {
  get tag() { return this._tag || 'link'; },
  set tag(v) { this._tag = v; }
};
const lnk = Object.create(proto);
lnk.tag = 'link';
lnk.href = 'https://fonts.gstatic.com';
Object.defineProperty(lnk, 'rel', {
  get() { return this.getAttribute('rel'); },
  set(v) { this.setAttribute('rel', v); this._relSet = true; }
});
console.log(lnk.rel);
lnk.rel = 'preconnect';
console.log(lnk.rel, lnk._relSet);
