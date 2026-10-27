let log=[];
class C{
  static{#init(){
    log.push('init');
    return;
  }}
  static x=(()=>{log.push('field');C.#init();})();
}
console.log(log.join('|'));
