# Define an exception called OopsException. Raise this exception to see what happens. Then write the code to catch this exception and print Caught an oops.

div_num = int(input("Enter a number: "))
div_num2 = int(input("Enter a 2nd number: "))

while div_num:
        try:
            result = div_num / div_num2
            if result != 0:
                print(result)
                break
        except Exception as OopsException:
                print("Caught an oops.")
                raise OopsException        
        