#WordIndex.py
#Name: Afrah Mohamoud
#Date: 03/01/2026
#Assignment: Lab 6
import string


def normalize_word(word):
  return word.strip(string.punctuation).lower()


def build_word_index(file_name):
  word_index = {}

  with open(file_name, 'r') as text_file:
    line_number = 0

    for line in text_file:
      line_number += 1
      words = line.split()

      for word in words:
        clean_word = normalize_word(word)

        if clean_word == "":
          continue

        if clean_word not in word_index:
          word_index[clean_word] = [line_number]
        elif line_number not in word_index[clean_word]:
          word_index[clean_word].append(line_number)

  return word_index


def print_word_index(word_index):
  for word in sorted(word_index):
    line_numbers = ", ".join(str(number) for number in word_index[word])
    print(f"{word}: {line_numbers}")

def main():
  file_name = input("Enter a file name (e.g., fish.txt or gettysberg.txt): ").strip()

  file_aliases = {
    "gettybergs.txt": "gettysberg.txt"
  }
  file_name = file_aliases.get(file_name.lower(), file_name)

  if file_name == "":
    print("Error: file name cannot be empty.")
    return

  try:
    word_index = build_word_index(file_name)
  except FileNotFoundError:
    print("Error: file not found.")
    return
  except OSError:
    print("Error: unable to open file.")
    return

  print_word_index(word_index)


if __name__ == '__main__':
  main()
