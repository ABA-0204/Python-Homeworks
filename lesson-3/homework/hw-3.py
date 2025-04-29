###list and tuple

#Create a list containing five different fruits and print the third fruit.
fruits=['pineapple','orange','grape','pear','kiwi']
print(fruits[3:4:])

#Create two lists of numbers and concatenate them into a single list.
list_1=[1,3,5,7]
list_2=[2,4,6,8]
print(list_1+list_2)

#Given a list of numbers, extract the first, middle, and last elements and store them in a new list.
list1=[1,2,3,4,5,6]
newlist=[list1[0:1:]+list1[3:4:]+list1[-1::]]
print(newlist)
#Create a list of your five favorite movies and convert it into a tuple.
movies=['devil wears prada','1+1','spring summer fall winter... and spring']
my_tuple=tuple(movies)
type(my_tuple)
#Given a list of cities, check if "Paris" is in the list and print the result.
cities=['London','NYC','Seoul','Moscow']
if 'Paris' in cities:
    print('yes')
else:
    print('no')

#Create a list of numbers and duplicate it without using loops.
numbers=[1,2,3,4,5]
numberscopy=numbers.copy()
print(numberscopy)
#Given a list of numbers, swap the first and last elements.
numbers=[1,2,3,4,5]
numbers[0]='new first value'
numbers[-1]='new last value'
print(numbers)
#Create a tuple of numbers from 1 to 10 and print a slice from index 3 to 7.
numbers_t=1,2,3,4,5,6,7,8,9,10
print(numbers_t[3:7:])
#Create a list of colors and count how many times "blue" appears in the list.
colors=['white','blue','black']
colors.count('blue')

#Given a tuple of animals, find the index of "lion".
animals='lion','cat','dog'
animals.index('lion')
#Create two tuples of numbers and merge them into a single tuple.
tuple1=1,3,5,7,9
tuple2=2,4,6,8,10
print(tuple1+tuple2)

#Given a list and a tuple, find and print their lengths.
len(list1)
len(tuple2)
#Create a tuple of five numbers and convert it into a list.
numbers_5=12,23,34,45,56
list_5=list(numbers_5)
type(list_5)

#Given a tuple of numbers, find and print the maximum and minimum values.
max(numbers_5)
min(numbers_5)
#Create a tuple of words and print it in reverse order.
words='life','luck','heart','team'
print(words[::-1])



