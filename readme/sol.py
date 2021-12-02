from solution_checker import check_key

PLAIN = "origin.txt"
ODD = "new.txt"

target = "{hey_that_is_the_great_puzzle}"

def genLetterDict():
	res_dict = {}
	plaintext = open(PLAIN).read().lower()
	oddText = open(ODD).read()
	for i in range(len(plaintext)):
		letter = plaintext[i]
		if letter not in res_dict:
			res_dict[letter] = set()
		res_dict[letter].add(oddText[i])
	return res_dict

def genAllOptions(letter_dict):
	letter_dict['_'] = set('_')
	letter_dict['{'] = set('{')
	letter_dict['}'] = set('}')
	options = [[]]
	for letter in target:
		extensions = []
		for arr in options:
			for i, possible_letter in enumerate(letter_dict[letter]):
				if i == 0:
					arr.append(possible_letter)
				else:
					new_arr = arr.copy()
					new_arr[-1] = possible_letter
					extensions.append(new_arr)
		options.extend(extensions)

	res = [''.join(option) for option in options]
	return res

def checkAllOptions(all_options):
	key_checker_data = open("key_checker_data", "rb").read()
	possible_result = []
	for option in all_options:
		if check_key(option, key_checker_data):
			possible_result.append(option)
	return possible_result

def main():
	res_dict = genLetterDict()
	all_options = genAllOptions(res_dict)

	possible_results = checkAllOptions(all_options)
	for result in possible_results:
		print(result)

if __name__ == '__main__':
	main()