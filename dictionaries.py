### {}  Dictionaries {}
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(days[3])

days = {
    "January": 31,
    "February": 28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31,
}
print(days["February"])

d = {"A": 100, "B": 200}
d["C"] = 300  ## Add 'C' value
d["A"] = 400  ## Change the value of 'A'
# del d['A']    ## To delete value 'A'
print(d["A"])
print(d["B"])
print(d["C"])

x = {"dog": "has a tail and goes woof!", "cat": "says meow", "mouse": "chased by cats"}

word = input("Enter a word: ")
print("The definition is : ", x[word])

dictionaries = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}
letter = input("Eneter Roman number: ").capitalize()

print(f"Roman number {letter} is {dictionaries[letter]}")

deck = [
    {"value": i, "suit": c}
    for c in ["spade", "clubs", "diamond", "hearts"]
    for i in range(2, 15)
]

print(deck[51]["value"])
print(deck[51]["suit"])

### 11.3 Working With Dictionaries
d = {"A": 100, "B": 200, "C": 300, "D": 400, "E": 500, "F": 600}
letter = input("Enter a letter: ").capitalize()
if letter in d:
    print("The value is", d[letter])
else:
    print("Not in dictionary")

for key in d:
    print(key)
    print(d[key])
    print(key, d[key])

### Statement                Result                Description
### list(d)               ['A','B']                keys of d
### list(d.values())      [1,3]                    values of d
### list(d.items())       [('A',1),('B',3)]        (key,value) pairs of d


### 11.4 Counting Words
# lines = open("test.txt").read()
lines = open("/home/solomon/Documents/chapter-11/test.txt").read()
lines = [line.strip() for line in open("/home/solomon/Documents/chapter-11/test.txt")]
print(lines)  ## Print original file.

from string import punctuation

lines = lines.lower()
for p in punctuation:
    lines = lines.replace(p, "")
words = lines.split()
print(len(word))  ### Count how many words on the file.
print(words)

d = {}
for w in words:
    if w in d:  ### Count words and duplicate words.
        d[w] += 1
    else:
        d[w] = 1

print(d)


with open("/home/solomon/Documents/chapter-11/test.txt") as file:
    content = file.read()
    print(content)

## print in alphabetical order
d = {"D": 100, "B": 200, "A": 300, "F": 400, "E": 500, "C": 600}
items = list(d.items())
items.sort()
for i in items:
    print(i)

## print in order from least to most common
d = {"D": 100, "B": 200, "A": 300, "F": 400, "E": 500, "C": 600}
items = list(d.items())
items = [(i[1], i[0]) for i in items]
items.sort()
for i in items:
    print(i)

