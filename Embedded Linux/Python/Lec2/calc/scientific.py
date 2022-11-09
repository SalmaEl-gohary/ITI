import math

def Add():
	#take operands from user
	x = int(input("Enter first number: "))
	y = int(input("Enter second number: "))
	
	#calculate result and print it to stdout
	print("Result is {}.".format(x+y))
	
def Sub():
	#take operands from user
	x = int(input("Enter first number: "))
	y = int(input("Enter second number: "))
	
	#calculate result and print it to stdout
	print("Result is {}.".format(x-y))
	
def Mul():
	#take operands from user
	x = int(input("Enter first number: "))
	y = int(input("Enter second number: "))
	
	#calculate result and print it to stdout
	print("Result is {}.".format(x*y))
	
def Div():
	#take operands from user
	x = int(input("Enter first number: "))
	y = int(input("Enter second number: "))
	
	#check for Division by zero
	if (y == 0):
		print("Can't divide by zero");
		return
		
	#calculate result and print it to stdout
	print("Result is {}.".format(x/y))
	
def Mod():
	#take operands from user
	x = int(input("Enter first number: "))
	y = int(input("Enter second number: "))
	
	#check for Division by zero
	if (y == 0):
		print("Can't divide by zero");
		return
		
	#calculate result and print it to stdout
	print("Result is {}.".format(x%y))

def Abs():
	#take operands from user
	x = int(input("Enter Your number: "))
	
	#check for negative numbers
	if (x < 0):
		x = x * -1
		
	#calculate result and print it to stdout
	print("Result is {}.".format(x))

def Inverse():
	#take operands from user
	x = int(input("Enter Your number: "))
	
	#check for Division by zero
	if (x == 0):
		printf("Can't divide by zero!")
		return 
		
	#calculate result and print it to stdout
	print("Result is {}.".format(1/x))

def Square():
	#take operand from user
	x = int(input("Enter Your number: "))
	
		
	#calculate result and print it to stdout
	print("Result is {}.".format(x*x))
	
def root():
	#take operand from user
	x = int(input("Enter Your number: "))
		
	#calculate result and print it to stdout
	print("Result is {}.".format(math.sqrt(x)))
	
def power():
	#take operands from user
	x = int(input("Enter number for base: "))
	y = int(input("Enter number for power: "))
	
		
	#calculate result and print it to stdout
	print("Result is {}.".format(math.pow(x,y)))
	
