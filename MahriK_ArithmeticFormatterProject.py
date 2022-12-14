# First, I need to define a function
# Second, I need to separate the incoming user input
# Third, I need to calculate the number of dashes through the length function = len(biggest number) +1+1
#Fourth, I need to implement the requirements such as: limit of five problems, limit to only add or subtract, limit to only have numeral input, limit of digit width of 4 numbers,


def arithmetic_arranger(problems, option=False):
    print(problems) 
    
    if len(problems)>=6: 
        print("Error: Too many problems.")    
        return  
    
    for user_input in problems:
        if len(user_input)<3: 
            print("Not enough input.")
            return

        operand1=user_input.split(" ")[0]
        arith_sign=user_input.split(" ")[1]
        operand2=user_input.split(" ")[2]
        print(arith_sign)    

        if arith_sign=="*" or arith_sign=="/":   
            print("Error: Operator must be '+' or '-'.")
            return
        
        if operand1.isdigit()==False or operand2.isdigit()==False:
            print("Error:Number must only contain digits.")
            return
        
        if len(operand1)>4 or len(operand2)>4:
            print("Error: Numbers cannot be more than four digits.")
            return

    print(problems)

    operand1=[]
    operand2=[]
    arith_sign=[]
    diff=[]
    dashes=[]
    calc=[]
    

    for problem in problems:
        operand11=problem.split(" ")[0]   # placing the first number to empty list
        operand1.append(operand11)

        arithmetic=problem.split(" ")[1] # placing the sign  to empty list
        arith_sign.append(arithmetic)

        operand22=problem.split(" ")[2]  # placing the second number to empty list
        operand2.append(operand22)

        if arithmetic=="-":
            calc1=int(operand11)-int(operand22)  # calculating and placing resutlt to empty list
            calc.append(calc1)
        else:
            calc1=int(operand11)+int(operand22)  # calculating and placing resutlt to empty list
            calc.append(calc1)
                

        maxnum=max(int(operand11),int(operand22))  # calculating the width difference to determine spaces later
        diff1=len(operand11)-len(operand22)
        diff.append(diff1)
        
        dash=len(str(maxnum))+2  # calculatting dashes needed for
        dashes1='-'*dash  
        dashes.append(dashes1)
    print("Here is the calculation of operands:\n ", calc)    

 # Here we are trying to calculate the spaces in the first line and second line
    top__leading_spaces=[]
    bottom_leading_spaces=[]
    for difference in diff:
        if difference>0:
            bottom_leading_spaces.append(difference*" ")
            top__leading_spaces.append("")
        else:
            top__leading_spaces.append(abs(difference)*" ")
            bottom_leading_spaces.append("")    
    
    # Now we will try to print the first line 
    top_string=""
    for i in range(len(operand1)):
        empty_space=top__leading_spaces[i]
        num=str(operand1[i])
        top_string+="  "+empty_space+num+"    "

    middle_string=""
    #middle_string2=""
    for i in range(len(operand2)):
        empty_space=bottom_leading_spaces[i]
        num=str(operand2[i])
        sign=str(arith_sign[i])
        middle_string+=sign+" "+empty_space+num+"    "    
        #middle_string2+=" "*len(sign)+empty_space+" "*len(num)+"    "
    bottom_string=""
    for i in range(len(dashes)):
        dashes1=str(dashes[i])
        bottom_string+=dashes1+"    "

    optional_string=""
    for i in range(len(calc)):
        optional_string1=str(calc[i])
        optional_space=len(dashes[i])-len(optional_string1)
        optional_string+=" "*optional_space+optional_string1+" "*4

   
    # print(operand1,operand2,arith_sign,diff,dashes) # Testing
    # print("Here are the spaces:", top__leading_spaces, bottom_leading_spaces) # Testing 
    print(top_string + "\n" + middle_string +"\n" + bottom_string + "\n" + (optional_string if option==True else ""))
  
    
    

arithmetic_arranger(["10 - 30", "20 + 80", "1 - 1", "9999 - 9999", "0 - 9999"])  # make it so that it accepts any amount of problems, but  prints out the needed statement and continues with using only the first 5 

