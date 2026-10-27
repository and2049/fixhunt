const o = {'__proto__': {toString(){return 'changed'}}}, p = {}; Object.assign(p, o); console.log(p.toString());
