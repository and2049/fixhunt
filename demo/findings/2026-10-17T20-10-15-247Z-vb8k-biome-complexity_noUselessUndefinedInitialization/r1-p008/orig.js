function process(input) {
  let data = undefined; // Rule triggers
  console.log('data == null:', data == null);
  console.log('data === null:', data === null);
  console.log('data ?? "default":', data ?? 'default');
  console.log('data || "fallback":', data || 'fallback');
  
  const obj = { value: 42 };
  console.log('obj.prop?.length:', obj.prop?.length);
  console.log('obj[data]?.prop:', obj[data]?.prop);
}

process();

// Show difference if data were null
data = null;
console.log('\nWith null:');
console.log('data == null:', data == null);
console.log('data === null:', data === null);
console.log('data ?? "default":', data ?? 'default');
console.log('data || "fallback":', data || 'fallback');
}
