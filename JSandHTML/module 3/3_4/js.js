// آرایه از اسامی
const names = ['جان', 'پاول', 'جونز'];

// کد HTML برای اضافه کردن
let htmlCode = '';
for (const name of names) {
  htmlCode += `<li>${name}</li>`;
}

// افزودن کد HTML به المان هدف
document.getElementById('target').innerHTML = htmlCode;
