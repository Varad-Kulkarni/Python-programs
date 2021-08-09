#Python program to demonstrate list and tuples.Also,all operations on them and fine maximum of list
lists = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] #Creating list
print(lists[2:5])  #Accessing specific elements from lists
lists.insert(4, "watermelon")  #Changing list items
print(lists)
lists.append("orange")  #Adding elements to list
print(lists)
lists.remove("banana")  #Removing list items
print(lists)
for x in lists:  #Looping list
  print(x)
lists.sort()  #Sorting lists
print(lists)
mylist = lists.copy()  #Copying lists
print(mylist)
list1 = ["a", "b", "c"]  #Joining list
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

tuples = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")  #Creating tuple
print(tuples[2:5])  #Accessing specific elements in tuples
y = list(list1)  #Update tuple
y[1] = "kiwi"
list1 = tuple(y)
print(list1) 
(green, yellow, red) = list1  #Unpack tuples
print(green)
print(yellow)
print(red)
for x1 in tuples:  #Looping tuple
  print(x1)
tuple1 = ("a", "b" , "c")  #Joining tuple
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

lis = [1, 10, 40, 36, 16] #Finding largest number in the list
lis.sort()
print("Largest number in the list is:", lis[-1]) 
 

