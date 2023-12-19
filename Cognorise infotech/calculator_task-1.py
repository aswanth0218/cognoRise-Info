print('******calculator*******')
print('***choice operator***')
print("1.addition")
print('2.subtraction')
print('3.multiplication')
print('4.division')

operator = input('choice operation : ')

num1 = int(input('NUM 1 : '))
num2 = int(input('NUM 2 : '))

if operator == '1':
    add = num1+num2
    print(f"Addition of Number :{add}")
    
elif operator == '2':
    subtract = num1-num2
    print(f"subtract of Number :{subtract}")
    
elif operator == '3':
    multiplication = num1*num2
    print(f"multiplication of Number :{multiplication}")
    
elif operator == '4':
    division = num1/num2
    print(f"Addition of Number :{division}")
    
else:
    print("choice the correct operator")
    

    

    

