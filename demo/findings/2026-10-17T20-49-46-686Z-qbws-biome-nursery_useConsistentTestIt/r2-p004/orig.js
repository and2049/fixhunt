function App() {
  return (
    <div>
      {test<span>hello</span>}
    </div>
  );
}
// Simulate JSX execution: treat as object creation
try {
  const el = { type: 'div', props: { children: [{ type: 'span', props: { children: 'hello' }}] } };
  console.log('JSX-like structure created:', el.props.children[0].props.children);
} catch (e) {
  console.log('Error:', e.name, e.message);
}
