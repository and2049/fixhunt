// Hazard 7: TDZ check - using let before declaration in same block
if (true) {
  console.log(typeof temp); // should be undefined due to TDZ
  let temp = \"\" + \"value\";
  console.log(temp);
}
