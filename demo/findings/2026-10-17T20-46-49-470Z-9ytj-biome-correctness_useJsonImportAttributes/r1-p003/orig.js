try {
  import { nonExistentProp } from './data.json';
  console.log('unreachable');
} catch (e) {
  console.log(e.name + ': ' + e.message);
}
