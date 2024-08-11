def evenOrOdd(num: int):
    # if(num % 2 == 0):
    #     return str(num) +' is  an even number'
    # return str(num) +' is an odd number'

    #ternery operator
    return str(num) +' is  an even number' if num % 2 == 0 else str(num) +' is an odd number'

number = int(input('Enter the number:'))

print(evenOrOdd(number))