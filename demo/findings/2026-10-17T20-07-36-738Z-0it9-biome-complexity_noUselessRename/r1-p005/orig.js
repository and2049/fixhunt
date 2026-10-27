const o = { m() { return this.x; }, x: 20 };
const { m: m } = o;
try { console.log(m()); } catch (e) { console.log(e.name + ': ' + e.message); }
