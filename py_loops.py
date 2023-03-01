# -- While loop --

number = 7
play = input("Would you like to play? (Y/n) ")

while play != "n":
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!")

    play = input("Would you like to play? (Y/n) ")


# -- The break keyword --

while True:
    play = input("Would you like to play? (Y/n) ")

    if play == "n":
        break  # Exit the loop

    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly!")
    elif abs(number - user_number) == 1:
        print("You were off by 1.")
    else:
        print("Sorry, it's wrong!")


# -- For loop --

friends = ["Rolf", "Jen", "Bob", "Anne"]
for friend in friends:
    print(f"{friend} is my friend.")

# -- For loop 2 -- Average

grades = [35, 67, 98, 100, 100]
total = 0
amount = len(grades)

for grade in grades:
    total += grade

print(total / amount)

# -- Rewritten using sum() --

grades = [35, 67, 98, 100, 100]
total = sum(grades)
amount = len(grades)

print(total / amount)

### A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ['John', 'Paul', 'Sara', 'Susan']

# Simple for loop
for person in people:
  print(f'Current Person: {person}')

# Break
for person in people:
  if person == 'Sara':
    break
  print(f'Current Person: {person}')

# Continue
for person in people:
  if person == 'Sara':
    continue
  print(f'Current Person: {person}')

# Continue
for person in people:
  if person == 'Sam':
    pass
  print(f'Current Person: {person}')

# range
for i in range(len(people)):
  print(people[i])

for i in range(0, 11):
  print(f'Number: {i}')

# While loops execute a set of statements as long as a condition is true.

count = 0
while count < 10:
  print(f'Count: {count}')
  count += 1

##
# combining else with while
count = 0
while (count < 3):
    count = count + 1
    print("Hello Geek")
else:
    print("In Else Block")

# combining else with for
 
list = ["geeks", "for", "geeks"]
for index in range(len(list)):
    print(list[index])
else:
    print("Inside Else Block")