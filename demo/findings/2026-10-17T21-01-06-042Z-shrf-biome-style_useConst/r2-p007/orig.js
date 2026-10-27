"use strict";
try { let v = 1; v = 2; } catch (e) { console.log(e.name); }
(function() { "use sloppy"; let w = 1; w = 2; console.log(w); })();
