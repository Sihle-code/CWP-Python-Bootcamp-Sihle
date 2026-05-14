#  List are used to store multiple items in a single variable.

# Create a list of 5 fruits and print the list.

fruit = ["Banana", "Apple", "Kiwi", "Peach", "Orange"]
print(fruit)    

#  Add a new fruit to the end of the list using append()
# Appen happens at the end of the list..
fruit.append("Watermeelon")
print(fruit)

#Insert a fruit at position 2 in your list.
# Always add an index number to insert a fruit at a specific position in the list.
fruit.insert(2, "Litchi")
print(fruit)

# 4. Remove the last item from the list using pop(). 
# Use an integer index to remove a specific item from the list. If no index is specified, pop() removes and returns the last item in the list.
fruit.pop(6)
print(fruit)

#  5. Remove a specific fruit from the list using remove().
fruit.remove('Peach')
print(fruit)

