function Component() {
  const { className } = {};
  return <div className={className || 'default'}></div>;
}
console.log(typeof Component);
