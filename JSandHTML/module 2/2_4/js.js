// درخواست اعداد از کاربر تا زمانی که صفر وارد کند
const numbers = [];

// Ask the user for numbers until they input zero
while (true) {
    const number = parseFloat(prompt("Enter a number (or 0 to stop):"));
    if (number === 0) {
        break; // Exit the loop if 0 is entered
    } //lisää listaan
    numbers.push(number);
}

// järjestää numeroa isosta pieneen
numbers.sort((a, b) => b - a);

// ایجاد یک sring برای نمایش اعداد مرتب شدهCr
let outputHTML = "<h2>Numbers from largest to smallest:</h2><ul>";
numbers.forEach(number => {
    outputHTML += `<li>${number}</li>`;
});
outputHTML += "</ul>";

/// نمایش اعداد مرتب شده در سند HTMLment
document.getElementById("output").innerHTML = outputHTML;
