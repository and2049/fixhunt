const proto = { get a() { return 1; } };
let obj = { __proto__: proto, a: 2 };
console.log(obj.a); // 2
obj = undefined;
try { obj.a; } catch (e) { console.log('member access:', e.name); }
try { const x = obj.a; } catch (e) { console.log('destructuring would throw:', e.name); }
