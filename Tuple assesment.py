#Write a python program to create a tuple.
# t1=(1,2,3,4,5,6)
# print(t1)
# t2=("apple", 2, 3.5, True)
# print(t2)

# #Write a python program to create a tuple with different data types.
# t3=("John", 26,8.8, "New York",[1,2,3], {"name"})
# print(t3)

#Write a python program to create a tuple with numbers and print one item.
# t4=(10,20,30,40,50)
# print(t4[3],t4[2])
# t5=(11,12,13,14,15,26,[43,87])
# print(t5[3],t5[6])

# #Write a python program to unpack a tuple in several variables.
# tuple=("Vaishnavi",23, "Jalna", "Student")
# name, age,city, profession=tuple
# print("Name:", name)
# print("Age:",age)
# print("City:",city)
# print("Profession:",profession)

# #Write a python program to add an item in a tuple.
# t6=("pen","pencil","book")
# print("Previous tuple:", t6)
# list=list(t6)
# list.append("scale")
# t6=(list)
# print("New tuple:",t6)

#Write a program to reverse a tuple.
# mytuple=(1,2,3,4,5,6)
# reversed_tuple=mytuple[::-1]
# print("Reversed tuple:", reversed_tuple)

#Write a python program to check whether an element exists within a tuple.
# t1=(1,2,3,4,5)
# print("Tuple:",t1)
# def check_element(t,element):
#     if element in t:
#          print(f"{element} exists in the tuple.")
#     else:
#         print(f"{element} does not exist in the tuple.")

# check_element(t1,2)
# check_element(t1,7)
        
#Write a python program to convert a list to a tuple.
# a=[11,12,13,14,15]
# print("list:", a)
# mytuple=tuple(a)
# print("Tuple:",a)

#Write a program to slice a tuple.
mytuple=(1,2,3,4,5,6,7,8,9)
sliced_tuple= mytuple[2:6]
print("Original tuple:",mytuple)
print("Slicedtuple:",sliced_tuple)

#Perform len(),sum(),max(),min(),operation on python.

numbers =[1,2,3,4,5]
length = len(numbers)
print("length of the list:",length)

numbers =[1,2,3,4,5]
total = sum(numbers)
print("Sum of the list:",total)

numbers=[1,2,3,4,5]
max_value = max(numbers)
print("Maximum value in the list:",max_value)

numbers=[1,2,3,4,5]
min_value=min (numbers)
print("Minimum value in the list:", min_value)


         


