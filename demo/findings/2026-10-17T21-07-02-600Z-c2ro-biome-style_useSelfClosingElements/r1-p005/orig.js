const props = { children: 'bad' };
const comp = ({ children }) => children || 'ok';
console.log(<div {...props}>{comp(props)}</div>);
