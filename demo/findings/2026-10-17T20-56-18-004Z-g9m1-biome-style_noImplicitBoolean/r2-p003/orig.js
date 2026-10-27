// Hazard 3: Getter side effect toggling JSX implicit boolean
const obj = {
  get disabled() {
    console.log('getter called');
    return true;
  }
};
console.log('before:');
const el = <input disabled={obj.disabled} />;
console.log('after:');
