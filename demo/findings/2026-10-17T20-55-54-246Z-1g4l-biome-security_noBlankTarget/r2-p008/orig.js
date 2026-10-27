const btn = (
  <a
    href="/url"
    target="_blank"
    className="btn"
  >
    submit
  </a>
); console.log(btn.type === 'a' && btn.props.target === '_blank');
