# Lab Challenge: Number Conversion

## Objective:

Write a program that converts a user input (a number) into its word equivalent. The primary goal is to handle numbers between 0 and 99.

### Requirements:

1. The user should input a number between 0 and 99.
2. Your program should output the word representation of the number.
   - For example:
     - Input: `23`
     - Output: `Twenty-Three`

## Challenge 1: Extend to Hundreds

1. Modify your program to handle numbers between 0 and 999.
   - For example:
     - Input: `532`
     - Output: `Five Hundred Thirty-Two`

## Challenge 2: Roman Numerals

1. Instead of outputting words, convert the number to its Roman numeral representation.

   - For example:
     - Input: `25`
     - Output: `XXV`

### Tips:

- Consider using functions to break down the problem.
- Create lists or dictionaries for number-word mappings. This will be especially useful for the numbers 1-19 and the tens (20, 30, 40, etc.).
- For the Roman numeral challenge, remember the following symbols and their values:
  - I - 1
  - V - 5
  - X - 10
  - L - 50
  - C - 100
  - D - 500
  - M - 1000