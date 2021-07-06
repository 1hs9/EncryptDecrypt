def Encryption(z):
    z = z.replace(' ', '')
    binary_list = []
    cipher_test = []
    lii = list(z)
    for lett in lii:
        kk = ord(lett)
        binary = bin(kk).replace('0b', '')
        binary_list.append(binary)

    binary_encode = str(''.join(binary_list))
    binary_encode_list = (list(binary_encode))
    print('\nbinary_encode: ' + binary_encode)
    key = list('1'*int(len(binary_encode)))

    for i in range(len(binary_encode_list)):
    	kk = str(int(binary_encode_list[i])^int(key[i]))
    	cipher_test.append(kk)
 
    cipher = str(''.join(cipher_test))
    print('\ncipher: ' + cipher)    	
    


Encryption(input('Input string to encodes: '))