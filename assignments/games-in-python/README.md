

# 📘 Assignment: Hangman Game

## 🎯 Objective

Build a classic Hangman game in Python. Practice string manipulation, loops, conditionals, and random selection by creating a word-guessing game where players try to reveal a hidden word before running out of attempts.

## 📝 Tasks

### 🛠️	Create the Hangman Game

#### Description
Write a Python program that lets a player guess letters to reveal a hidden word. The game should track correct and incorrect guesses, display progress, and end with a win or lose message.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list
- Accept letter guesses from the player
- Show current progress using underscores for unguessed letters (e.g. _ a _ _ m a n)
- Track and display the number of incorrect guesses remaining
- End when the word is fully guessed or attempts are exhausted
- Display a win message if the player guesses the word, or a lose message if they run out of attempts

Example:
```
Word: _ a _ _ m a n
Guesses left: 4
Guessed letters: a, m, n
Enter your guess: g
```

### 🛠️	Enhance the Game (Optional)

#### Description
Add extra features to make your Hangman game more fun and user-friendly.

#### Requirements
Completed program could:

- Allow the player to choose difficulty (word length or number of attempts)
- Show a list of incorrect guesses
- Prevent repeated guesses
- Add ASCII art for the hangman
