const o = { valueOf: () => '5', toString: () => 'o' };
console.log(+{} + String(o));
// Expected: NaNo // After fix: '+String(o)' -> concatenation
