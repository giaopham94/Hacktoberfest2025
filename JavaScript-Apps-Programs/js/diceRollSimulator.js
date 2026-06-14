// File: diceRollSimulator.js
// Author: Dheeraj (Hacktoberfest 2025)
// Description: Simulate dice roll (1–6).

function rollDice() {
  return Math.floor(Math.random() * 6) + 1;
}

// Example usage
alert("🎲 You rolled a " + rollDice());
