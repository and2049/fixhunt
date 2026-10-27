// logger fn
const logger = {
  msg: 'test',
  // log it
  log: function() { return this.msg; }
};
const fn = logger.log;
console.log(fn.call(logger));
// arrow escape
const arrow = () => this.msg;
console.log(arrow.call({msg: 'other'}));
