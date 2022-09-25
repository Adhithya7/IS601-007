#UCID: 31584791
#Date: 09/24/2022

a1 = [-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]
a2 = [-1, 1, -2, 2, 3, -3, -4, 5]
a3 = [-0.01, -0.0001, -.15]
a4 = ["-1", "2", "-3", "4", "-5", "5", "-6", "6", "-7", "7"]

def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nPositive Output:\n")
    #The function converts each element in the array to its positive equivalent
    #It also ensures that the final type is unchanged
    temp_arr = []
    for elem in arr:
        if isinstance(elem, (int,float)):
           temp_arr.append(abs(elem)) #abs returns the absolute value of the given value
        else:
            current_type = type(elem)
            try:
                temp_arr.append(current_type(abs(int(elem))))
            except:
                temp_arr.append(current_type(abs(float(elem))))   
            #Casting is done before and after conversion
    print(temp_arr)


print("Problem 3")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)