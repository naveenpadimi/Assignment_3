def string_test(s):
    case_counter={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           case_counter["UPPER_CASE"]+=1
        elif c.islower():
           case_counter["LOWER_CASE"]+=1
        elif c==int:
            pass
        else:
           pass
    print ("Original String : ",input_string)
    print ("No. of Upper case characters : ", case_counter["UPPER_CASE"])
    print ("No. of Lower case Characters : ", case_counter["LOWER_CASE"])

input_string = str(input("Enter the string: "))
string_test(input_string)