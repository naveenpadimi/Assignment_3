input_string = str(input("enter the string : "))
def reverse(k):
    stringg =""
    for i in k:
        stringg = i+stringg
    return stringg
print("Original string : ",input_string)
print("Reversed string : ",reverse(input_string))