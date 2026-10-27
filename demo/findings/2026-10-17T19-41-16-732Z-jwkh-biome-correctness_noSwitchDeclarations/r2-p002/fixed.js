function f(){
  const regex = /a/g;
  switch('aa'){case 'aa': { let m = regex.exec('aa'); console.log(m.index); break;}}
}
