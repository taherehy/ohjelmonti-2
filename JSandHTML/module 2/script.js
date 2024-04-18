
'use strict';

const numbers = [];

// ;; ikuinen loopi, joka pyytää käyttäjältä numeroita

for (;;) {
    const number = parseInt(prompt('Enter a number:'));

    // Jos käyttäjä syöttää numeron, joka on jo annettu, ohjelma ilmoittaa, että numero on jo annettu ja lopettaa toimintansa

    if (numbers.includes(number)) {
        console.log('The number has already been given.');
        break;
    }

    // Lisätään annettu numero taulukkoon

    numbers.push(number);
}

// Tulostetaan kaikki annetut numerot nousevassa järjestyksessä

numbers.sort((a, b) => a - b);
console.log(numbers);
