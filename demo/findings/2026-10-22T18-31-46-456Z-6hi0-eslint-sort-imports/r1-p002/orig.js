// Hazard 2: async/await and generator interaction
async function fetch() { return Promise.resolve(1); }
import { fetch } from './async-mod'; // might be moved
import * as gen from './generator-mod'; // has generator that yields after import
(async () => {
  const a = await fetch();
  const it = gen.gen();
  console.log(a, it.next().value);
})();
