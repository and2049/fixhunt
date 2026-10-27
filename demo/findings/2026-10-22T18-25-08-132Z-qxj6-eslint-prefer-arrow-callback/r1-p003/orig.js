class Base{constructor(){this.pub=1;}getPub(){return this.pub;}}
class Der extends Base{constructor(){super();this.#priv=2;}
  get(){return this.#priv + super.getPub();}}
#DerPrv;let d=new Der();console.log(d.get());
