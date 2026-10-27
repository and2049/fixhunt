const Button = ({ className, children }) => {
  return <button className={className}>{children}</button>;
};
const el = <Button className='btn'>hi</Button>;
console.log(el.props.className); // Should be 'btn'
// After fix: becomes <Button class='btn' ...> -> React component ignores 'class' prop, so className becomes undefined
console.log('After fix simulation:', (<Button class='btn' />).props.className);
