let str = '111110111'; let regex = /(\d+)/g; regex.lastIndex = 0; let result = str.replace(regex, (m) => parseInt(m, 2)); console.log(result);
