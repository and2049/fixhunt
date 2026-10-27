// Internal Vue shared exports a regex utility used for template parsing
let TemplateRegex;
// --- Rule target ---
import { compileTemplate } from '@vue/shared'; // expect_trigger=true
// --------------------
TemplateRegex = /<\s*([a-zA-Z]+)/gu;
TemplateRegex.lastIndex = 0;
const match = TemplateRegex.exec('<div>hello</div>');
console.log(match ? match[1] : null);
