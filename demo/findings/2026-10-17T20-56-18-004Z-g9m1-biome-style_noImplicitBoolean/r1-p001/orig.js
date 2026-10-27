function bad() { throw new Error('fail'); }
try {
  console.log(<div onclick={() => bad()} hidden />);
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
