// Array of names
const names = ['John', 'Paul', 'Jones'];

// Target element
const targetElement = document.getElementById('target');

// HTML code to be added
let htmlCode = '';
for (const name of names) {
  htmlCode += `<li>${name}</li>`;
}

// Adding HTML to the target element
targetElement.innerHTML = htmlCode;
