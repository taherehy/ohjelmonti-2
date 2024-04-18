// ایجاد المان لیست
const firstItem = document.createElement('li');
firstItem.textContent = 'آیتم اول';

const secondItem = document.createElement('li');
secondItem.textContent = 'آیتم دوم';
secondItem.classList.add('my-item'); // افزودن کلاس به المان دوم

const thirdItem = document.createElement('li');
thirdItem.textContent = 'آیتم سوم';

// افزودن المان ها به المان با شناسه target
document.getElementById('target').appendChild(firstItem);
document.getElementById('target').appendChild(secondItem);
document.getElementById('target').appendChild(thirdItem);
