"use sloppy";
try { Object.assign({}, undefined) } catch(e) { console.log(e.name) }
"use strict";
try { Object.assign({}, undefined) } catch(e) { console.log(e.name) }
try { {} = { ...undefined } } catch(e) { console.log(e.name) }
