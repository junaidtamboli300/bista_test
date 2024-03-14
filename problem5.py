
import math

inputlist = [2.6743,3,6.3526,4.2323,5.9687,6.3265]

# def roundup(inputlist):
#     for i in range(len(inputlist)):
#         print(round(inputlist[i]))
# roundup(inputlist)




def my_func(inputlist):
    for i in range(len(inputlist)):
        print(round(inputlist[i]))

map(my_func(inputlist),inputlist)

