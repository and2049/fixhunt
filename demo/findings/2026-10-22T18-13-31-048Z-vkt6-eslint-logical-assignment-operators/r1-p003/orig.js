async function f() {
  let x = false;
  console.log(await x ||= Promise.resolve(1));
  console.log(x);
}
f().then(() => console.log('done'));
