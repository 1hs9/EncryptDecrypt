def Decryption(binary_encode):
	empty = []
	final_list = []
	newlii = []
	binary_encode_list = (list(binary_encode))
	# print binary_encode_list
	# print len(binary_encode_list)

	count = 0
	count1 = 0
	while count < len(binary_encode_list):
		count2 = count1+6
		while count1<=count2:
			try:
				empty.append(binary_encode_list[count1])
				count1+=1
			except IndexError:
				break
		string_encode = ''.join(empty)
		# print string_encode
		empty = []
		newlii.append(string_encode)
		count+=7

	# print newlii

	for each_encode in newlii:
		try:
			letter = (chr(int(each_encode, 2)))
		except ValueError:
			pass
		final_list.append(letter)
		# print (letter)

	print (''.join(final_list))


Decryption(str(input('Enter encode to decode: ')))


