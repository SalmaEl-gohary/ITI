from scientific import * 
from programmer import * 

while True:
	print("Choose Mode: ")
	print("	1- Scientific\n	2- Programmer\n	3- Exit")
	mode = int(input("Enter your choice: "))
	
	if mode == 1:
		print("Choose operation: ")
		print("				1- Add		2- Sub		3- Mul		4- Div\n\
				5- Mod		6- Abs		7- Inverse	8- Sq\n\
				9- square root	10- power")
				
		op = int(input("Enter your choice of op: "))
		if (op == 1):
			Add()
		elif (op == 2):
			Sub()
		elif (op == 3):
			Mul()
		elif (op == 4):
			Div()
		elif (op == 5):
			Mod()
		elif (op == 6):
			Abs()
		elif (op == 7):
			Inverse()
		elif (op == 8):
			Square()
		elif (op == 9):
			root()
		elif (op == 10):
			power()

		else:
			print("Op not defined! ")
		
	elif mode == 2: 
		print("Choose operation: ")
		print("				1- Shift >>		2- shift <<		3- AND\n\
				4- OR |		5- XOR ^		6- NOT\n\
				7- HEX		8- OCT		9- BIN")
		op = int(input("Enter the operation id: "))
		
		if (op == 1):
			Shift_R()
		elif (op == 2):
			Shift_L()
		elif (op == 3):
			AND()
		elif (op == 4):
			OR()
		elif (op == 5):
			XOR()
		elif (op == 6):
			NOT()
		elif (op == 7):
			get_hex()
		elif (op == 8):
			get_oct()
		elif (op == 9):
			get_bin()
		else:
			print("Op not defined! ")
				
	elif mode == 3:
		break
