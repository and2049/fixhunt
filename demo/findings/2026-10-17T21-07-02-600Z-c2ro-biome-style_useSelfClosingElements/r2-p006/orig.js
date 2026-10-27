const items = ['a', 'b'];
const fragments = items.map((item, index) => {
  return <>key={index}</>;
});
console.log(fragments[0].props.key === 0 ? 'ok' : 'broken');
