var z = 9;
import { z } from './one.js'; // exports { z: 1 }
{ 
  console.log(z);
  try { z = 2; } catch(e) { console.log(e.name); }
}
