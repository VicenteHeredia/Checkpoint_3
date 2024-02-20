# Exercise 1: Create a string, number, list, and boolean, each stored in their own variable.
print()
name = "Exercise 1 <answer>"
print(name)

# string
print()
sentence = "The quick brown fox jumps over the lazy dog"
print(sentence)

# number
print()
add = (2+3)
print(add)

#list
print()
list = ['one', 'two', 'three', 'four', 'five']
print(list)

# boolean
print()
print(sentence.isnumeric())

print()
# Exercise 2: Use an index to grab the first 3 letters in your string, store that in a variable.
name = "Exercise 2 <answer>"
print(name)
print()
print(sentence[0:3])


# Exercise 3: Use an index to grab the first element from your list.
print()
name = "Exercise 3 <answer>"
print(name)
print()

the_first = list[0]
print(the_first)

# Exercise 4: Create a new number variable that adds 10 to your original number.
print()
name = "Exercise 4 <answer>"
print(name)
print()

my_number = 23
add = my_number + 10
print(add)


# Exercise 5: Use an index to get the last element in your list.
print()
name = "Exercise 5 <answer>"
print(name)
print()

the_last = list[-1]
print(the_last)

# Exercise 6: Use split to transform the following string into a list.
# 	names = 'harry,alex,susie,jared,gail,conner'
print()
name = "Exercise 6 <answer>"
print(name)
print()

tags = 'harry, alex, susie, jared, gail, conner'
list_of_tags = tags.split(',')
print(list_of_tags)

# Exercise 7: Get the first word from your string using indexes. Use the upper function to transform the letters into uppercase. Create a new string that takes the uppercase word and the rest of the original string.
print()
name = "Exercise 7 <answer>"
print(name)
print()

# first_word = list_of_tags [0]
# print(first_word)
# print(tags.upper())
# print(tags.title())

tags_two = tags.replace ('harry', 'HARRY')
print(tags_two)

print()

t = list_of_tags [0]
u = list_of_tags [1]
w = list_of_tags [2]
x = list_of_tags [3]
y = list_of_tags [4]
z = list_of_tags [5]
tags_three = t.upper(), u, w, x, y, z
print(tags_three)

# Exercise 8: Use string interpolation to print out a sentence that contains your number variable.
print()
name = "Exercise 8 <answer>"
print(name)
print()

my_number = add
sentence = f'My number variable is {add}.'
print(sentence)

print()

my_number = add
sentence = 'My number variable is {0}.'.format(my_number)
print(sentence)

# Exercise 9: Print “hello world”.
print()
name = "Exercise 9 <answer>"
print(name)
print()

print('hello world')
print()