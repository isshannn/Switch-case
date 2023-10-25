def check_input(argument):
    
    if(argument.isalpha()):
        print("Invalid input alphabet") 
        exit(0)

    elif (argument.isdecimal()):
        x = int(argument)
        return x
    
    else:    
        return argument
    
def case_check(argument):
    match argument:
        case 1: return a+b
        case 2: return a-b
        case 3: return a*b
        case 4: return a/b
        case default: return "Invalid choice";

print("1: Addition")
print("2: Substraction")
print("3: Multiplication")
print("4: Division")
print("Enter your choice: ")

c = input()
if(not c.isdecimal()):
    print("Inavalid Input")
    exit(0)
c = check_input(c)


print("Enter the values of a and b")
a = input()
a = check_input(a)
b = input()
b= check_input(b)
c = case_check(c)
print(c)