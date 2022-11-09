import time
import os

#height = int(input("Enter height of pyramid: "))
height = 5

#draw right direction arrow
def right(height):
	spaces_arrow = (height * 3) + 2
	lines = (height * 2)
	spaces_pyramid = (height + 2)
	
	print("\n" * lines)

	#draw first half pyramid
	for i in range(1,height + 1):
		print("  " * spaces_arrow, end="")  	
		print("  " * spaces_pyramid, end = "")			  	
		print("* " * i)								  

	#middle Line
	print("  " * spaces_arrow, end="")	  	
	print("* " * spaces_arrow)			  	

	#draw second half-pyramid
	for i in range(height, 0, -1):
		print("  " * spaces_arrow, end = "")  
		print("  " * spaces_pyramid, end = "")			
		print("* " * i)
	

	
#draw down direction arrow
def down(height):
	spaces_arrow = (height * 2) + 2
	lines = (height * 3) 
	total = spaces_arrow + height
	
	print("\n" * lines)
	#draw middle line before pyramid starts
	print(((("  " * total ) + "*\n") * (height + 2)), end="")
	
	#draw reversed pyramid
	for i in range(height,0,-1):
		spaces = height - i + spaces_arrow
		stars = i * 2 + 1
		print("  " * spaces, end = "")
		print("* " * stars)
		
	#draw middle-line after pyrmid
	print(((("  " * total ) + "*\n") * (height)), end="")	

#draw left direction arrow
def left(height):

	longest_line = (height * 3) + 2
	lines = (height * 2) 
	print("\n" * lines)

	#draw first half-pyramid
	for i in range(1, height+1):
		spaces = (height - i) + height + 2
		print("  " * spaces, end="")
		print("* " * i)
		
	#draw middle line
	print("  ", end="")
	print("* " * longest_line)
	
	#draw second half-pyramid
	for i in range(height, 0, -1):
		spaces = (height - i) + height + 2
		print("  " * spaces, end="")
		print("* " * i)
		
#draw upward direction arrow
def up(height):
	spaces_arrow = (height * 2) + 2
	total = spaces_arrow + height
	

	#draw middle line before pyramid starts
	print(((("  " * total ) + "*\n") * (height)), end="")
	
	#draw pyramid
	for i in range(1, height + 1):
		spaces = height - i + spaces_arrow
		stars = i * 2 + 1
		print("  " * spaces, end = "")
		print("* " * stars)
		
	#draw middle-line after pyrmid
	print(((("  " * total ) + "*\n") * (height + 2)), end="")	
	


#switch
while True:
	right(height)
	time.sleep(1)
	os.system("cls")

	down(height)
	time.sleep(1)
	os.system("cls")

	left(height)
	time.sleep(1)
	os.system("cls")
	
	up(height)
	time.sleep(1)
	os.system("cls")

