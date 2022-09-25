#UCID: 31584791
#Date: 09/24/2022

a1 = [10.001, 11.591, 0.011, 5.991, 16.121, 0.131, 100.981, 1.001]
a2 = [1.99, 1.99, 0.99, 1.99, 0.99, 1.99, 0.99, 0.99]
a3 = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
a4 = [10.01, -12.22, 0.23, 19.20, -5.13, 3.12]


def process_array(num, arr):
    print("\nProcessing Array({}): \n\n".format(num))
    print(arr)
    total = 0.00
    #Function calucates the sum of an array (upto 2 decimal point precision)
    #The function also takes into consideration the floating point precision issue in python
    for num in arr:
        total += num*1000 
        #Multiplied by 1000 since the numbers in the array have max 3 floating points
    total = '%.2f'%round(total/1000, 2) 
    print("\nThe total is : {}\n".format(total))

print("Problem 2")
process_array(1, a1)
process_array(2, a2)
process_array(3, a3)
process_array(4, a4)