const wasmStr = '(module (func (result i32) (i32.const -0)))';
console.log(wasmStr.includes('-0') ? 'has negative zero' : 'does not');
