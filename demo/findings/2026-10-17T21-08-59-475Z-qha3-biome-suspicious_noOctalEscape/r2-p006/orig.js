const s = `\\251`; // intended: backslash + '251'
console.log(s, s.length);
// After bad fix: would become `\u00A9` (c.r) + '251'? No — but rule shouldn't fire here.
// Actual issue: if code had `\251` without double backslash, rule fires but shouldn't.
// So we show a case where it should NOT fire but might be misapplied.
console.log(s === '\\251' ? 'ok' : 'broken');
