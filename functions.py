import cgi,re
USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASSWORD_RE = re.compile("^.{3,20}$")
EMAIL_RE = re.compile("^[\S]+@[\S]+.[\S]+$")


def rot13(text):
        alphabets = {"a":"n","b":"o","c":"p","d":"q","e":"r","f":"s","g":"t","h":"u","i":"v","j":"w","k":"x","l":"y","m":"z","n":"a","o":"b","p":"c","q":"d","r":"e","s":"f","t":"g","u":"h","v":"i","w":"j","x":"k","y":"l","z":"m"}
        alphabets_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m"]
        rot13 = ""
        test_text = cgi.escape(text,quote=True)
        print test_text
        for i in text:
                if i != " " and ord(i) > 63 and ord(i) < 123:
                        if i.islower():
                                get_letter = alphabets[i]
                                rot13 += get_letter
                        else :
                                get_letter = alphabets[i.lower()]
                                rot13 += get_letter.upper()
                elif i == " ":
                        rot13 += (" ")
                else:
                        i = cgi.escape(i, quote=True)
                        rot13 += i

        return rot13


def valid_username(username):
    return USER_RE.match(username)

def valid_password(password):
    return PASSWORD_RE.match(username)

def valid_email(email):
    return EMAIL_RE.match(username)