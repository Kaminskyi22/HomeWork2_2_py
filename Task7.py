num1=int(input("Enter number 1 :"))
num2=int(input("Enter number 2 :"))

if num1==num2:
    print("Numbers are equal")
else:    
    if num1>num2:
        print(f"Numbers in ascending order {num1} , {num2}")
    else:
        print(f"Numbers in ascending order {num2} , {num1}")