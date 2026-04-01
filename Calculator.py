#calculator.py
#Carter Grandcolas

# This is a calculator that can calculate three step equations instead of just two.
# The "i" runs throught the tokens and looks for the operation listed in the "if" function.
#If not found the i+= 1 line sends the code to the next loop.

calculator_input = input("Insert your calculation here (use spaces ex: 2 + 4 * 6):")

tokens = calculator_input.split()

i = 0
while i < len(tokens):
    if tokens[i] == '*':
        result = int(tokens[i-1]) * int(tokens[i+1])
        tokens[i-1:i+2] = [str(result)]
        i = 0
    elif tokens[i] == '/':
        b = int(tokens[i+1])
        if b == 0:
            print("Zero is not a valid divisor")
            exit()
        result = int(tokens[i-1]) / b
        tokens[i-1:i+2] = [str(result)]
        i = 0
    else:
        i += 1

i = 0
while i < len(tokens):
    if tokens[i] == '+':
        result = int(tokens[i-1]) + int(tokens[i+1])
        tokens[i-1:i+2] = [str(result)]
        i = 0
    elif tokens[i] == '-':
        result = int(tokens[i-1]) - int(tokens[i+1])
        tokens[i-1:i+2] = [str(result)]
        i = 0
    else:
        i += 1

i = 0
while i < len(tokens):
    if tokens[i] == '^':
        result = int(tokens[i-1]) ** int(tokens[i+1])
        tokens[i-1:i+2] = [str(result)]
        i = 0
    else:
        i += 1

calculator_output = tokens[0]

print(calculator_input, "=", calculator_output)
