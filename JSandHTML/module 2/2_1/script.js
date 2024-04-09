
'use strict';
//kutsutaan numeroita
const numbers = []

// pyytää numero ja lisää listaan
// با استفاده از دستور prompt از کاربر عدد می‌پرسیم

for(let i = 0; i < 5; i++) {
    numbers[i] = parseInt(prompt(`Number ${i + 1}: `));
}


// اعداد را به ترتیب معکوس چاپ می‌کنیم
for( let i = numbers.length-1; i >= 0;i--) {
  console.log(`${numbers[i]}`)
    //اعداد را چاپ می‌کنیم
}
