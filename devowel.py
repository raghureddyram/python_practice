state_list = ["Alabama", "California", "Texas"]
vowels = list('aeiou')


def devowel_1():
	output = []
	for state in state_list:
		state_letters = list(state.lower())

		for vowel in vowels:
			while True:
				try:
					state_letters.remove(vowel)
				except:
					break
		output.append("".join(state_letters).capitalize())

	return output


def devowel_2():
	output = []
	for state in state_list:
		consonants = ""
		for letter in state:
			letter = letter.lower()
			if letter not in vowels:
				consonants += letter
		output.append(consonants.capitalize())
	return output

print("Now printing output 1: {}".format(devowel_1()))
print("Now printing output 2: {}".format(devowel_2()))