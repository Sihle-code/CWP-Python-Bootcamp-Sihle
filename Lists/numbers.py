
# 6. Create a list of numbers and sort it in ascending order. 
#By default, the list is sorted in alphabetical or numerical order depending on the type of elements in the list

numbers = [8,20,6,2,15, 30, 8, 11, 2, 2, 16]
print(numbers)

# 7. Reverse the order of a list using reverse().

numbers.reverse()
print(numbers)

#  8. Count how many times a number appears in a list using count().
# This method takes one required argument: the value you want to count

count = numbers.count(2)
print(numbers[2])


#  9. Find the index of a specific element in a list using index(). 
# This method takes one required argument: the value you want to find the index of.
index = numbers.index(15)
print(index)




# 10. Create two lists and combine them into one lis

number1 = [5, 6, 1, 18, 7,]
number2 = [8, 9, 10, 4, 16]
combined_numbers = number1 + number2
print(sorted(combined_numbers))
