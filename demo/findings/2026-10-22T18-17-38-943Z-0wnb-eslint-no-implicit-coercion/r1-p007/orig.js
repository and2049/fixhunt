outer: for(let i=0;i<2;i++){
  for(let j=0;j<2;j++){
    if(j===1) continue outer;
    let x = +'';
    console.log(i+j+x);
  }
}
