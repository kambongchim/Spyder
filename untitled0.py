import string

def check(x):
  word = "".join(sorted(x.lower())).strip()
  dic = {}
  for l in word:
    if l in string.ascii_letters:
      dic[l] = dic.get(l, 0) + 1
  for k, v in dic.items():
    print(k, v)

check("Write a program that reads a string and returns a table of the letters of the alphabet in alphabetical order which occur in the string together with the number of times each letter occurs. Case should be ignored. A sample output of the program when the user enters the data “ThiS is String with Upper and lower case Letters”, would look this this")