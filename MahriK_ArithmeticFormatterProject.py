# Owner: Mahri Kadyrova
# This is the Arithmetic formatter project based off the FreeCodeCamp projects and "Scientific Computing with Python" course  

def arithmetic_arranger(problems, option=False):
    # This function takes key variable "problems" and defined variable "option"  
    print(problems) # Testing if the "problems" array was identified correctly  
    
    if len(problems) >= 6:
        print("Error: Too many problems.")
        return
    
    for user_input in problems:
        if len(user_input) < 3: 
            print("Not enough input.")
            return

        operand1 = user_input.split(" ")[0] # Obtaining an array with first operands only  
        arith_sign = user_input.split(" ")[1] # Obtaining an array with arihtmetic signs only  
        operand2 = user_input.split(" ")[2] # Obtaining an array with second operands only  

        if arith_sign == "*" or arith_sign == "/":   
            print("Error: Operator must be ' + ' or ' - '.")
            return
        
        if operand1.isdigit() == False or operand2.isdigit() == False:
            print("Error:Number must only contain digits.")
            return
        
        if len(operand1) > 4 or len(operand2) > 4:
            print("Error: Numbers cannot be more than four digits.")
            return

# The next cluster of lines creates empty lists of to be utilized later to obtain operand 1 list, operand 2 list, arithmetic sign list, width difference between two operands list, number of dashes needed list, and a list with performed calculations  
    operand1 = []
    operand2 = []
    arith_sign = []
    diff = []
    dashes = []
    calc = []

    for problem in problems:
        operand11 = problem.split(" ")[0]  # placing the first number (aka operand 1) to empty list  
        operand1.append(operand11)

        arithmetic = problem.split(" ")[1]  # placing the sign  to empty list  
        arith_sign.append(arithmetic)

        operand22 = problem.split(" ")[2]  # placing the second number (aka operand 2) to empty list  
        operand2.append(operand22)

        if arithmetic == " - ":
            calc1 = int(operand11) - int(operand22)  # calculating and placing the subtraction calculation to "calc" list  
            calc.append(calc1)
        else:
            calc1 = int(operand11) + int(operand22)  # calculating and placing the addition calculation to "calc" list  
            calc.append(calc1)

        maxnum = max(int(operand11),int(operand22))  # calculating the width difference to determine the space needed in front of operand 1 and operand 2  
        diff1 = len(operand11) - len(operand22)
        diff.append(diff1)
        
        dash = len(str(maxnum)) + 2  # calculatting dashes needed for artihmetic formatter
        dashes1 = "-" * dash  
        dashes.append(dashes1)

    print("Here is the calculation of operands:\n ", calc)    

 # Code to calculate the spaces in the first and second lines  
    top__leading_spaces = []
    bottom_leading_spaces = []

    for difference in diff:
        if difference > 0:
            bottom_leading_spaces.append(difference * " ")
            top__leading_spaces.append("")
        else:
            top__leading_spaces.append(abs(difference) * " ")
            bottom_leading_spaces.append("")    
    
    # Creating a string to print for the first line of arithmetic formatter
    top_string = ""

    for i in range(len(operand1)):
        empty_space = top__leading_spaces[i]
        num = str(operand1[i])
        top_string += "  " + empty_space + num + "    "

# Creating a string to print for the middle line of arithmetic formatter
    middle_string = ""
    
    for i in range(len(operand2)):
        empty_space = bottom_leading_spaces[i]
        num = str(operand2[i])
        sign = str(arith_sign[i])
        middle_string += sign + " " + empty_space + num + "    "    
        # middle_string2 += " "*len(sign) + empty_space + " "*len(num) + "    "

# Creating a string to print for the bottom line of the arithmetic formatter
    bottom_string = ""

    for i in range(len(dashes)):
        dashes1 = str(dashes[i])
        bottom_string += dashes1 + "    "

# Creating a string to print for the optional line of arithmetic formatter
    optional_string = ""

    for i in range(len(calc)):
        optional_string1 = str(calc[i])
        optional_space = len(dashes[i]) - len(optional_string1)
        optional_string += " "*optional_space + optional_string1 + " "*4
   
    print(top_string + "\n" + middle_string + "\n" + bottom_string + "\n" + (optional_string if option == True else ""))
  
# The input to call the arithmetic_arranger function
arithmetic_arranger(["10 - 30", "20 + 80", "1 - 1", 
                     "9999 - 9999", "0 - 9999"])
