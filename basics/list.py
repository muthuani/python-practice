#A List in Python is an ordered collection of items that can store different data types (numbers, strings, etc.).
#It is mutable, meaning you can change, add, or remove items after creating it.

fruits = ["apple", "banana", "mango"]   # list of strings
numbers = [10, 20, 30, 40]             # list of integers
mixed = [1, "Ria", 3.14, True]         # mixed data types
print("fruits list has string values =",fruits)
print("numbers list has numeric values =",numbers)
print("This is mixed list has string, numeric, float, boolean values =",mixed)


mylist = ["apple","banana","cherry","grapes"]

print(f"List of fruits = {mylist}")
print(f"Length of the List = {len(mylist)}")
mylist.insert(1,"pineapple")

print(f"Added an item in the position 1 using insert function = {mylist}")


print(f"List using index position 2 = {mylist[2]}")

print(f"List using negative index last item = {mylist[-1]}")

mylist.append("Kiwi")
mylist.append("Watermelon")

print(f"Added 2 items  to List using append = {mylist}")

print(f"List Displaying 2 alternative item = {mylist[::2]}")

mylist.remove("cherry")

print(f"List after removing cherry using remove = {mylist}")
l2=mylist[2:4]
print("Assigning some value from current list to new list using slicing [2:4] =",l2)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3,4,5,90,10]

list3 = list1 + list2

print(f"Max value of List2 = {max(list2)} and Min value of List2 = {min(list2)}")
print("Created new list3 adding list1 + list2 =",list3)
print("Multiply list1 using * by 3 times",list1*3)