// Hazard 1: Comment inside concat lost if stripped
const s = \"start\" /* middle */ + \"end\";
console.log(s);
