#DiceRoll.py
#Name: Afrah Mohamoud 
#Date: 03/01/2026
#Assignment: Lab 6
import random

def main():
  # Create an empty list to store counts for sums 2 through 12
  rolls = [0] * 13
  total_rolls = 36000

  # Roll two dice total_rolls times
  for _ in range(total_rolls):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)

    # Find the sum total of the two dice and count it
    roll_sum = die1 + die2
    rolls[roll_sum] += 1

  # Print statistics for dice rolls
  print("Sum\tCount\tPercent")
  for roll_sum in range(2, 13):
    percent = (rolls[roll_sum] / total_rolls) * 100
    print(f"{roll_sum}\t{rolls[roll_sum]}\t{percent:.2f}%")


if __name__ == '__main__':
  main()
