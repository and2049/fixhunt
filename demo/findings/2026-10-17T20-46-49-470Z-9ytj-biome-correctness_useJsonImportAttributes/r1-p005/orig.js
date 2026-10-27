import cfg from './data.json';
class C {
  static field = cfg.value;
  constructor() {
    console.log(C.field);
  }
}
new C();
