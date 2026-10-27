// Logger fn
const logger = {
  msg: 'test',
  // Log it
  log: function() { return this.msg; }
};
const fn = logger.log;
console.log(fn.call(logger));
// Arrow escape
const arrow = () => this.msg;
console.log(arrow.call({msg: 'other'}));
