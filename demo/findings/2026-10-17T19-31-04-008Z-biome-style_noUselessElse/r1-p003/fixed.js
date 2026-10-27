async function f() {
  if (true) return await Promise.resolve(1);
  
    console.log('skipped');
    return 2;
}
f().then(console.log);
