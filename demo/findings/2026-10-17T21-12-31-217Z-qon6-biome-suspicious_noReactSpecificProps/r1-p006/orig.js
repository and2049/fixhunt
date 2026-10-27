const props = { className: 'spread', id: 'x' };
const el = <div {...props} className='explicit' />;
console.log(el.props.className); // In React, later wins -> 'explicit'
// After fix: becomes <div {...props} class='explicit' /> but props.className still spreads -> two attributes
// We can't render, so show that props has className and we spread it
console.log('props has className:', !!props.className);
