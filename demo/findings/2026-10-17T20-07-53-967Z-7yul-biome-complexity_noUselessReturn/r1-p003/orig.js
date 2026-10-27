async function f(){
  console.log('start');
  await Promise.resolve();
  console.log('mid');
  return;
}
f().then(()=>console.log('end'));
