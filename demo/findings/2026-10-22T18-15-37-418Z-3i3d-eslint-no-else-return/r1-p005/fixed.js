function timingTest(val) {
  console.log('start:', typeof y); // Hazard: accessing hoisted var
  if (val > 0) {                   // Trigger: if with return
    return y * 2;
  }                                
                             // Else with var decl
    var y = 5;                     // Hoisted to top
    y += val;
    return y;
  
}
console.log(timingTest(3));
console.log(timingTest(-1));
