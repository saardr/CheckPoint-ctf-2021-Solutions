import re


PATTERN = "x.xx...x.xxx..-xx-.xxxx.-.-xxx.-.x..x.xxxx..x.xxx.-.-.xx-.-xxx..-.xx.x.x.--x.xxx"

enc_dict = {
	'A':'.-', 'B':'-...',
	'C':'-.-.', 'D':'-..', 'E':'.',
	'F':'..-.', 'G':'--.', 'H':'....',
	'I':'..', 'J':'.---', 'K':'-.-',
	'L':'.-..', 'M':'--', 'N':'-.',
	'O':'---', 'P':'.--.', 'Q':'--.-',
	'R':'.-.', 'S':'...', 'T':'-',
	'U':'..-', 'V':'...-', 'W':'.--',
	'X':'-..-', 'Y':'-.--', 'Z':'--..',
	'1':'.----', '2':'..---', '3':'...--',
	'4':'....-', '5':'.....', '6':'-....',
	'7':'--...', '8':'---..', '9':'----.',
	'0':'-----', ', ':'--..--', '.':'.-.-.-',
	'?':'..--..', '/':'-..-.', '-':'-....-',
	'(':'-.--.', ')':'-.--.-'
}

def morseEncoderWithNoSpace(text):
	index_dict = {}
	curr_len = 0
	res_arr = []
	for letter in text:
		letter_morse = enc_dict[letter]
		res_arr.append(letter_morse)
		index_dict[curr_len] = letter
		curr_len += len(letter_morse)
	res_morse = ''.join(res_arr)
	return res_morse, index_dict


def morseDecoder(s):
	res = ""

	morse_dict = dict((v,k) for k, v in enc_dict.items())
	tmp = ""
	for letter in s + " ":
		if letter == " ":
	 		if tmp in morse_dict:
	 			res += morse_dict[tmp]
	 			tmp = ""
	 		else:
	 			return False, ""
		else:
			tmp += letter
	return True, res

def TranslateBook(filepath):
	book = open(filepath).read()
	book = re.sub(r'[^a-zA-Z0-9]', '', book)
	open("log.txt", "w").write(book)
	book = book.upper()
	book_morse, index_dict = morseEncoderWithNoSpace(book)
	re_pattern = PATTERN.replace('.', '\\.').replace('x', '.')
	res_match = re.search(re_pattern, book_morse)

	start = res_match.start(0)	
	end = res_match.end(0)
	res_decoded = []
	while start < end:
		letter = index_dict[start]
		start += len(enc_dict[letter])
		res_decoded.append(letter)

	return res_match, ''.join(res_decoded)
	#res_match = re.findall(re_pattern, book_morse)
	#return res_match

def main():
	res, res_decoded = TranslateBook("book.txt")
	print(res)
	print(res_decoded)

if __name__ == '__main__':
	main()
