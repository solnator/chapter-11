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