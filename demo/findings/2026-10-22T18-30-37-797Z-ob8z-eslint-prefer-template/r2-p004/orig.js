console.log(1 + 2 * '3' + 4); // Before: 1+(2*'3')+4 = 1+6+4=11
                      // After fix would be same due to precedence, but we test coercion:
console.log(typeof (1 + 2 * '3' + 4));
