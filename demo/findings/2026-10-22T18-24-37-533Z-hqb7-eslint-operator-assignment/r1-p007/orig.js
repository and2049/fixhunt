let x = 1
x = x
+ 2 // TRIGGER: ASI would break without fix? Actually x = x
+2 is invalid; but we rely on the fix changing behavior if applied incorrectly
// Instead, make a case where ASI affects
let y = 1
y = y
+ 3
console.log('x:', x, 'y:', y)
