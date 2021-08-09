file = open("Sample.txt", "r")

number_of_lines = 0
number_of_words = 0
number_of_characters = 0

def FindLen(Strin):
  count = 0
  for i in Strin:
    count += 1
  return count  
  
for line in file:

  line = line.strip("\n")
  words = line.split()
  number_of_characters += FindLen(line)

file.close()

print("characters are:", number_of_characters)