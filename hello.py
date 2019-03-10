def encoder_or_decoder(encode_string,plus_or_minus):
	encoded_text = ""
	if plus_or_minus.lower() == "zakoduvatu":
		for s in encode_string:
			r = ord(s)+1
			encoded_text = encoded_text + chr(r)
	else:
		for s in encode_string:
			r = ord(s)-1
			encoded_text = encoded_text + chr(r)


	print(encoded_text)


def output(z):
	print(z)