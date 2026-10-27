// Hazard 7: ASI risk - if await removed and no semicolon, next line '(' is absorbed
let x = 1
(await { click: () => console.log(x) }).click() // If no semicolon after 1, this is: 1(await...)
console.log('Survived')
