#UCID: 31584791
#Date: 09/24/2022

a1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a2 = [0, 1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
a3 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
a4 = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    print("\nOdds output:\n")
    #Function finds the odd numbers in the input array and prints the same (by using modulo)
    temp_arr = []
    for element in arr:
        if element % 2 != 0:
            temp_arr.append(element)
    print(temp_arr) 


print("Problem 1")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)