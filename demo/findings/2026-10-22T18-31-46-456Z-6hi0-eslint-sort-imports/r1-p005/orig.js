// Hazard 5: Comment preservation
// Keep this comment near b-import
import a from './mod'; /* keep me */
import b from './mod'; // TRIGGER: may be moved above a
console.log('keep me' in a ? 1 : 0);
