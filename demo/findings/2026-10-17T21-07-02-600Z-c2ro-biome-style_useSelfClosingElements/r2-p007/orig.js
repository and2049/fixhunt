// before
const el = <div></div><!-- note -->;
// after fix: <div /><!-- note --> becomes <div /> and comment is gone
console.log('comment presence affects minification safety');
