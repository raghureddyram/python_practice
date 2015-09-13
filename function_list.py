shopping_list = list()

def show_help():
	print("What to pick up at the store?")
	print("Enter 'DONE' to stop adding items. Enter HELP to ask for help.")

def add_to_list(item):
	shopping_list.append(item)
	print("Added! List has {} items.".format(len(shopping_list)))

def show_list():
	print("Here's your list:")
	for item in shopping_list:
		print(item)

show_help()

while True:
	new_item = input("> ")
	if new_item == "DONE":
		break
	elif new_item == "HELP":
		show_help()
		continue #necessary here, otherwise HELP will show as added to the list
	else:
		add_to_list(new_item)
	# continue
show_list()
	