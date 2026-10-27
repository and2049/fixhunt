async function f(){
  console.log('start');
  await Promise.resolve();
  console.log('mid');
}
f().then(()=>console.log('end'));
