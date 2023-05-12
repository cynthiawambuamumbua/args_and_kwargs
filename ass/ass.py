# Write a function that takes an unknown number of arguments and returns their sum.
def add_numbers(a, b):
    sum = a + b
    print(sum)

add_numbers(2, 3)
# Write a function that takes two arguments, the first being a string
# and the second being an unknown number of integers. The function
# should return a new string where the integers have been added to the original string.
def add_integers(string, *integers):
    result = string
    for integer in integers:
        integer += string
    return result
print(add_integers(12,13,15))

# Write a function that takes an unknown number of keyword arguments and 
# returns a dictionary where the keys are the argument names and the values are the argument values.
def return_dict(**names):
    return names
dict = return_dict(name="cynthia", age=19, city="nairobi")
print(dict)

# Write a function that takes a function and an unknown number of arguments
# , and returns the result of calling the function with the arguments.
def return_funtion(function,*args):
    return function(args)
args = (1,2,3,4,5)
print(args)
# Write a function that takes a list of integers and an unknown number of keyword arguments.
#  The function should return a new list where each integer in the
#  original list has been multiplied by the value of the corresponding keyword argument.
def multiply_list(list):
    result = 1
    for i in list:
        result = result * i
    return result
list1 = [1, 2, 3]
list2 = [3, 2, 4]
print(multiply_list(list1))
print(multiply_list(list2))


# Write a function that takes a list of integers and an unknown number of 
# additional integers as arguments. The function should return the index 
# of the first occurrence of the sum of the list and the additional integers
def occurence_sum_list(integers):
  total = 0
  for number in integers:
    total = total + number
  return total

my_list = [1,3,5,2,4]
occurence_sum_list(my_list)


# Write a function that takes an unknown number of keyword arguments, 
# each with a string value. The function should 
# concatenate all the strings and return the resulting string.
def concatenate_strings(number):
    number1="cynthia"
    number2="mumbua"
    print(concatenate_strings(number(number1+number2)))