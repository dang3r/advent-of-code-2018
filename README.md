# Advent of Code 2018

My solutions for Advent of Code 2018.

# Notes

# Problem 14

- my magic number was 440231. Since new recipes added are in the range [0, 18], to get my 0 meant the two elves
  would have to each find a recipe of 0.
- I typically printed out how many recipes there were on each iteration of the main while loop. This is awful for performance.
  Printing periodically was better.