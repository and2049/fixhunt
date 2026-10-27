var r = /\u{61}/gu; console.log(r.lastIndex, r.exec('a')); r.lastIndex = 0; console.log(r.lastIndex, r.exec('a'));
