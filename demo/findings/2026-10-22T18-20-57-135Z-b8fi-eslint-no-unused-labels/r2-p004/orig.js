// Labels cannot appear before 'use strict' in a way that would make it a directive prologue
// This is a near-miss: rule does not trigger because label cannot be before directive in same lexical unit
'use strict';
console.log('strict mode');
