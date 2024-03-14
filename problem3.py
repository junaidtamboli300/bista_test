def square(number):
    for i in range(len(number)):
        if number[i] >= 0:
          print(number[i] * number[i])
               
def cubes_negative(number):
    for i in range(len(number)):
        if number[i] < 0:
            print(number[i] * number[i] * number[i])
            
def absolute_integer(number):
    for i in range(len(number)):
        print(abs(number[i]))
    
def even_number_greater_than_ten(number):
    for i in range(len(number)):
        if number[i] > 10 and number[i] % 2 == 0:
            print(number[i])
            
numbers = [5,-8,12,-3,17,0,-10,6]
square(numbers)
# cubes_negative(numbers)
# absolute_integer(numbers)
# even_number_greater_than_ten(numbers)