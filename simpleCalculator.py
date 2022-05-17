operation = str(input("Enter an operation (addition, subtraction, multiplication, division or modulus): "))
firstNumber = int(input("Enter the first number: "))
secondNumber = int(input("Enter the second number: "))

if operation == 'addition': 
    print ('The sum of ', firstNumber, 'and', secondNumber, 'is', firstNumber + secondNumber)
    
elif operation == 'subtraction': 
    print ('The difference between ', firstNumber, 'and', secondNumber, 'is', firstNumber - secondNumber)
    
elif operation == 'multiplication': 
    print ('The product of ', firstNumber, 'and', secondNumber, 'is', firstNumber * secondNumber)
    
elif operation == 'division': 
    print ('The division ', firstNumber, 'and', secondNumber, 'is', firstNumber / secondNumber)
    
elif operation == 'modulus': 
    print ('The modulus of ', firstNumber, 'and', secondNumber, 'is', firstNumber % secondNumber)
else: 
    print ('This operation is not valid. Please try again and choose from the provided in the options')
