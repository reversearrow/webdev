from functions import rot13, valid_username, valid_password, valid_email,verify_password
import webapp2

rot13_form = """
<h2>Enter some Rot13 text here</h2>
<form method="POST">
<input type="text" name="text" value="%(text)s" style="height: 100px; width: 400px"></input><br>
<input type="submit">
</form>
"""

user_signup_form = """
<h2>User Signup</h2>
<form method="POST">
<label> Username <input type = "text" name = "username" value = "%(username)s"></input></label> <br>
<label> Password <input type = "password" name = "password" value = ""> </input></label> <br>
<label> Verify <input type = "password" name = "verify"> </input></label> <br>
<label> Email <input type = "text" name = "email" value = "%(email)s"> </input></label> <br>
<input type="submit">
<h2> %(error)s </h2>
"""

welcome_message = """
<h1> Welcome %(username)s.</h1>
"""


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, Udacity!')


class Rot13(webapp2.RequestHandler):
	def get(self):
        	self.response.write(rot13_form % ({"text":""}))
	def post(self):
		text = self.request.get("text")
		rot13_text = rot13(text)
		self.response.out.write(rot13_form % ({"text":rot13_text}))


class Signup(webapp2.RequestHandler):
	def write_form(self,username="",password="",email="",error=""):
		self.response.write(user_signup_form % ({"username":username,"password":password,"email":email,"error":error}))

	def get(self):
		self.write_form()

	def validate_input(self,username,password,verify,email):
		if not valid_username(username):
			error = "'%s' is not a valid username." % (username)
			self.write_form(username,password,email,error)
		elif not valid_password(password):
			error = "Password is not valid is not a valid password."
			self.write_form(username,password,email,error)
		elif not verify_password(password,verify):
			error = "Verify and Password doesn't match"
			self.write_form(username,password,email,error)
		elif not valid_email(email):
			error = "'%s' is not an valid email." % (email)
			self.write_form(username,password,email,error)
		else:
			self.redirect("/unit2/welcome?username=" + username)

	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")
		email = self.request.get("email")

		self.validate_input(username,password,verify,email)


class Welcome(webapp2.RequestHandler):
	def get(self):
		username = self.request.get("username")
		if valid_username(username):
			self.response.out.write(welcome_message % ({"username": username}))
		else:
			self.redirect("/unit2/signup")



app = webapp2.WSGIApplication([('/', MainPage),('/unit2/rot13',Rot13),('/unit2/signup',Signup),("/unit2/welcome",Welcome)], debug=True)
