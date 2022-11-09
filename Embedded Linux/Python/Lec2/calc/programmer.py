
def Shift_R():
	#take operands from user
	operand = int(input("Enter number to shift: "))
	shift = int(input("Enter shift value: "))
	
	#calculate result 
	res = operand >> shift;
	
	#print result 
	print("The result is {}.".format(res))
	
def Shift_L():
	#take operands from user
	operand = int(input("Enter number to shift: "))
	shift = int(input("Enter shift value: "))
	
	#calculate result 
	res = operand << shift;
	
	#print result 
	print("The result is {}.".format(res))
	
def AND():
	#take operands from user
	no1 = int(input("Enter first number: "))
	no2 = int(input("Enter second number: "))
	
	#calculate result 
	res = no1 & no2;
	
	#print result 
	print("The result is {}.".format(res))
	
def OR():
	#take operands from user
	no1 = int(input("Enter first number: "))
	no2 = int(input("Enter second number: "))
	
	#calculate result 
	res = no1 | no2;
	
	#print result 
	print("The result is {}.".format(res))
	
def XOR():
	#take operands from user
	no1 = int(input("Enter first number: "))
	no2 = int(input("Enter second number: "))
	
	#calculate result 
	res = no1 ^ no2;
	
	#print result 
	print("The result is {}.".format(res))

def NOT():
	#take operands from user
	no = int(input("Enter number to negate: "))
	
	#calculate result 
	res = ~no 
	
	#print result 
	print("The result is {}.".format(res))
	
def get_hex():
	#take operands from user
	no = int(input("Enter number to get HEX: "))
	
	#calculate result 
	res = hex(no)
	
	#print result 
	print("The result is {}.".format(res))
	
def get_oct():
	#take operands from user
	no = int(input("Enter number to get OCT: "))
	
	#calculate result 
	res = oct(no)
	
	#print result 
	print("The result is {}.".format(res))
	
def get_bin():
	#take operands from user
	no = int(input("Enter number to get BIN: "))
	
	#calculate result 
	res = bin(no)
	
	#print result 
	print("The result is {}.".format(res))

	
	