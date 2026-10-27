{
  const obj = { a: null };
  console.log(obj.a ?? 'null');
  console.log((obj.b ?? undefined) ?? 'undefined');
}
