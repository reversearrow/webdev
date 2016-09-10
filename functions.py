import cgi
def rot13(text):
        alphabets = {"a":"n","b":"o","c":"p","d":"q","e":"r","f":"s","g":"t","h":"u","i":"v","j":"w","k":"x","l":"y","m":"z","n":"a","o":"b","p":"c","q":"d","r":"e","s":"f","t":"g","u":"h","v":"i","w":"j","x":"k","y":"l","z":"m"}
	alphabets_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
	rot13 = ""
        test_text = cgi.escape(text,quote=True)
        print test_text
        for i in text:
                if i != " ":
                        if i.islower():
                                get_letter = alphabets[i]
                                rot13 += get_letter
                        else :
                                get_letter = alphabets[i.lower()]
                                rot13 += get_letter.upper()
                else:
                        rot13 += (" ")
        return rot13

