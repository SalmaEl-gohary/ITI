#ITI Shop 

products = [{'name': 'apple', 'q': 40, 'price': 15},{'name': 'banana', 'q': 40, 'price': 15},
 {'name': 'cherry', 'q': 40, 'price': 15}]
 
records = [[{'name': 'apple', 'q': 3, 'price': 15}],[]]


#loop over products dict and print details
def show_products(mode):
	for i in range(len(products)):
		print("\n")
		print(str(i), end="")
		print(" --> "+ products[i]['name'], end="")
		print(" ---> " + str(products[i]['price']) + " EGP", end="")
		if mode == 0:
			print(" ---> " + str(products[i]['q']) + " in stock")
	
	print("\n")
			

#get product info from owner
def add_product():
	name = input("Please Enter product name: ")
	
	price = input("Please Enter product price: ")
	quantity = input("Enter the quantity in stock: ")
	product = {'name': name, 'price': price, 'q': quantity}
	products.append(product)
	
		
#edit quantity or price using product id 
def edit_product(option):
	show_products(0)
	id = int(input("Enter the id of the product you want to edit: "))
	if (id > len(products) - 1):
		print("Product doesn't exist!")
	else:
		if option == 0: #change price
			new_price = input("Enter the new price for {}: ".format(products[id]['name']))
			products[id]['price'] = new_price
			print("Price successfully edited! ")
		elif option == 1: #change quantity
			new_quantity = input("Enter the new quantity for {}: ".format(products[id]['name']))
			products[id]['q'] = new_quantity
			print("Quantity successfully edited! ")

#make new record and edit quantity in stock
def buy_product():
	purchase_id = len(records) - 1
	show_products(1)
	id = int(input("Enter the id of the item you want to buy: "))
	if (id < len(products)):
		quantity = int(input("Enter the quantity: "))
		if (quantity > products[id]['q']):
			print("Not enough in stock! ")
		else:
			print("You will pay {}EGP..".format(products[id]['price'] * quantity))
			affirm = input("continue?    y,n    ")
			if(affirm == 'y'):
				records[purchase_id].append({'name': products[id]['name'], 'q': quantity, 'price': products[id]['price']})
				products[id]['q'] -= quantity

				more = input("Do you want to buy other products?  y,n  ")
				if (more == 'y'):
					buy_product()
				else:
					print("purchase completed! your purchase id is {}. ".format(purchase_id))
					records.append([])

#use records to print bill with purchase id 
def print_bill():
	total = 0
	purchase_id = int(input("Please enter your purchase id: "))
	print("item		quantity		price 		total")
	for i in range(len(records[purchase_id])):
		name = records[purchase_id][i]['name']
		price = records[purchase_id][i]['price']
		quantity = records[purchase_id][i]['q']
		total += price * quantity
		print("{}		{}			{}		{}".format(name, quantity, price, price * quantity))
		
	print("total =  {} EGP".format(total))

print("Welcome to ITI shop!")
print("Select Mode: \n	For Customer mode press 1.")
print("	For Owner mode press 2.\n	To exit press 0.")	

choice = int(input("Enter your choice:"))


if choice == 1:
	#customer mode
	while(1):
		print("Customer:\n	To show our products press 1.")
		print("	To buy from our products press 2.")
		print("	To print the bill press 3.\n	To exit press 0.")
		
		choice = int(input("Enter your choice:"))
		if choice == 1:
			show_products(1)
		elif choice == 2:
			buy_product()
		elif choice == 3:
			print_bill()
		elif choice == 0:
			break
		
elif choice == 2:
	#owner mode 
	while 1:
		print("Owner:\n	To show products press 1.")
		print("	To Add new product press 2.\n	To Edit quantity press 3")
		print("	To change price press 4.\n	To exit press 0.")
		
		choice = int(input("Enter your choice:"))
		if choice == 1:
			show_products(0)
		elif choice == 2:
			add_product()
		elif choice == 3:
			edit_product(1) #edit quantity
		elif choice == 4:
			edit_product(0) #change price 
		elif choice == 0:
			break




	

	
