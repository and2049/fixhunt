let obj = { locator: () => ({ click: () => 'ok' }) };
let result = obj?.locator?.()?.click();
console.log(result);
obj = null;
result = await/* mark */ obj?.locator?.()?.click();
console.log(result);
