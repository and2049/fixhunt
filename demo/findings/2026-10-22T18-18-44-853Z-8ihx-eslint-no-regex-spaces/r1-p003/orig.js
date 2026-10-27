const base = { getPat: () => /test{2,}  end/ };
const obj = { __proto__: base };
obj.getPat = () => /test{2,}  end/;
let hits = 0;
for (let i = 0; i < 2; i++) {
  if (obj.getPat().test('testxx  end')) hits++;
}
console.log(hits);
