
total = 0
lst = []
lst_length = int(input("enter the length of the list : "))
for i in range(lst_length):
    numbers = int(input("Enter list : "))
    lst.append(numbers)
for i in range(lst_length):
	total = total + lst[i]
print("Sum of all elements in given list: ", total)
