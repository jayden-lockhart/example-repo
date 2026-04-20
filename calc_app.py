def calculations():
    while True:
        try:
            # get user to input 2 numbers and an operation
            num1 = float(input('enter a number: '))
            num2 = float(input('enter a number: '))
            operation = input('enter operation (+ - * /) ')

            # do calculation based on operation
            if operation == '+':
                total = num1 + num2
            elif operation == '-':
                total = num1 - num2
            elif operation == '*':
                total = num1 * num2
            elif operation == '/':
                total = num1 / num2
                if num2 == 0:
                    raise ZeroDivisionError('unable to divide by 0')
            else:
                raise ValueError('invalid operation')
            
            # write equation to equation.txt
            with open('equations.txt', 'a+', encoding='utf-8') as file:
                file.write(f'{num1} {operation} {num2} = {total} \n')
                break
        except (ValueError, ZeroDivisionError) as error:
            print(f'Error: {error} has occured')




def prev_calcs():
    #read file of previous calculations
    try:
        with open('equations.txt', 'r', encoding='utf-8') as file:
            equations = file.readlines() 
        # check for file
        if equations:
            print("\nPrevious equations:")
            for equation in equations:
                print(equation.strip())
        else:
            print("no previous equations found.")
    except FileNotFoundError:
        print("no previous equations")
     
    

def calc_app():
    # allow user to choose function
    while True:
            chioce = int(input('press 1 for calculation \t press 2 for previous calculations \t press 3 to exit'))
            if chioce == 1:
                calculations()
            elif chioce == 2:
                prev_calcs()
            elif chioce == 3:
                break
            else:
                print('invaid chioce')

calc_app()
