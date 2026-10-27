let arr1 = [, , 3];  // length 3, holes at 0,1
let arr2 = [1, 2, 3];
let sum = 0;
for (let i = 0; i < arr1.length; i++) {
  if (i >= 0 && i < arr2.length) {   // rule fires on 0 <= i : swap to i >= 0 (no change)
                                     // and on i < arr2.length : swap to arr2.length > i
    sum += (arr1[i] ?? 0) + (arr2[i] ?? 0);
  }
}
console.log(sum);  // Original: i=0: 0<=0 true, i<3 true → add (undefined??0)+1 = 0+1=1
                   //          i=1: 0<=1 true, i<3 true → add 0+2=2
                   //          i=2: 0<=2 true, i<3 true → add 3+3=6 → total=9
// Fix on i < arr2.length → arr2.length > i: same behavior
// Make it fire on left side: change to -1 < i
sum = 0;
for (let i = 0; i < 3; i++) {
  if (i > -1 && i < 3) {             // rule fires on -1 < i : swap to i > -1
    sum += (arr1[i] ?? 0) * (arr2[i] ?? 0);
  }
}
console.log(sum);  // Original: i=0: -1<0 true → include → 0*1=0
                   //          i=1: -1<1 true → 0*2=0
                   //          i=2: -1<2 true → 3*3=9 → total=9
// Fixed: i > -1 → same
// Need: make the swapped condition have side effect
let triggerLeft = 0;
function check() {
  triggerLeft++;
  return 5;
}
sum = 0;
for (let i = 0; i < 3; i++) {
  if (check() > i && i < 3) {        // rule fires on check() > i : swap to i < check()
    sum += i;
  }
}
console.log('sum:' + sum + '|triggerLeft:' + triggerLeft);  // Original: i=0: check()→5>0 true → sum+=0, triggerLeft=1
                                                              //          i=1: check()→5>1 true → sum+=1, triggerLeft=2
                                                              //          i=2: check()→5>2 true → sum+=2, triggerLeft=3 → sum=3
// Fixed: i < check()
//          i=0: 0<check()→5 true → sum+=0, triggerLeft=1 (check called)
//          i=1: 1<5 true → sum+=1, triggerLeft=2
//          i=2: 2<5 true → sum+=2, triggerLeft=3 → same
// Hazard: if check() had side effect that changed based on call order? Not here.
// Final: make check return i-dependent value
let callLog = '';
function checkVal(x) {
  callLog += 'c' + x;
  return x + 2;
}
sum = 0;
for (let i = 0; i < 3; i++) {
  if (checkVal(i) > i) {             // rule fires: swap to i < checkVal(i)
    sum += i;
  }
}
console.log('sum:' + sum + '|log:' + callLog);  // Original: i=0: checkVal(0)=2>0 true → sum+=0, log='c0'
                                                  //          i=1: checkVal(1)=3>1 true → sum+=1, log='c0c1'
                                                  //          i=2: checkVal(2)=4>2 true → sum+=2, log='c0c1c2' → sum=3
// Fixed: i < checkVal(i)
//          i=0: 0 < checkVal(0) → checkVal(0) called → log+='c0', returns 2 → 0<2 true → sum+=0
//          i=1: 1 < checkVal(1) → checkVal(1) → log+='c1', returns 3 → 1<3 true → sum+=1
//          i=2: 2 < checkVal(2) → checkVal(2) → log+='c2', returns 4 → 2<4 true → sum+=2 → same
// Still no difference because condition is pure and deterministic.
// Accept that for this hazard, behavioral change is rare, but we show interaction with loop and side effects in predicate.
console.log('end');
