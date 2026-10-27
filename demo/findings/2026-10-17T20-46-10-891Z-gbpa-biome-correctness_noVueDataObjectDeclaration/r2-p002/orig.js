let log = [];
log.push(1);
export default {
  data: {
    x: (log.push(2), 1),
    y: (log.push(3), 2)
  }
};
log.push(4);
console.log(log.join(','));
