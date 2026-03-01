#WordCount.py
#Name: Afrah Mohamoud
#Date: 03/01/2026
#Assignment: Lab 6

def count_file(file_name):
  try:
    with open(file_name, 'r') as text_file:
      line_count = 0
      word_count = 0
      char_count = 0

      for line in text_file:
        line_count += 1
        word_count += len(line.split())
        char_count += len(line)
  except FileNotFoundError:
    print(f"\nFile: {file_name}")
    print("Error: file not found.")
    return
  except OSError:
    print(f"\nFile: {file_name}")
    print("Error: unable to open file.")
    return

  print(f"\nFile: {file_name}")
  print(f"Lines: {line_count}")
  print(f"Words: {word_count}")
  print(f"Characters: {char_count}")

def main():
  file_name = input("Enter a file name (e.g., fish.txt, or ALL): ").strip()

  if file_name == "":
    print("Error: file name cannot be empty.")
    return

  if file_name.lower() == "all":
    count_file("gettysberg.txt")
    count_file("fish.txt")
    return

  count_file(file_name)
  

if __name__ == '__main__':
  main()
