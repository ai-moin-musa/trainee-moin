def repeated_words_from_sentence(string):
	new_string = ''
	words = [mul_word for mul_word in [word for word in string.split(" ")] if [word for word in string.split(" ")].count(mul_word) >= 2 ]
	words = set(words)
	return "#".join(words)


string = str(input("Enter string : "))

print(repeated_words_from_sentence(string))

