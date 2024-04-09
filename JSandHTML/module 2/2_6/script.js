const target = document.querySelector('#target');

// Function to generate a random number between 1 and 6 (inclusive)
function getRandom() {
  return Math.floor(Math.random() * 6) + 1;
}

// Infinite loop to continuously roll the dice until a condition is met
for (;;) {
  const dice = getRandom(); // Roll the dice
  target.innerHTML += `<p>Dice rolled: ${dice}</p>`; // Display the rolled value

  // Check if the rolled value is equal to 6
  if (dice === 6) {
    target.innerHTML += "<p>Condition met. Stopping.</p>"; // Display a message when the condition is met
    break; // Exit the loop
  }
}
