#python program to count number of characters ,words, and lines in given file .Also print each line of file in reverse order.

file = open("Sample.txt", "r")

number_of_lines = 0
number_of_words = 0
number_of_characters = 0
for line in file:
  line = line.strip("\n")

  words = line.split()
  number_of_lines += 1
  number_of_words += len(words)
  number_of_characters += len(line)

file.close()

print("lines:", number_of_lines, "words:", number_of_words, "characters:", number_of_characters)

textfile = open("Sample.txt")
lines = textfile.readlines()
for line in reversed(lines):
    print(line)