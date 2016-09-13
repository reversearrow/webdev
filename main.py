from functions import rot13, valid_username, valid_password, valid_email
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
<label> Username <input type = "text" name = "username" value = "%(username)s"> </input></label> <br>
<label> Password <input type = "password" name = "password" value = "%(password)s"> </input></label> <br>
<label> Verify <input type = "password" name = "verify"> </input></label> <br>
<label> Email <input type = "text" name = "email" value = "%(email)s"> </input></label> <br>
<input type="submit">
"""

welcome_message = """
<h1> Welcome %(username)s. Thank you for signing up. </h1>
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
	def write_form(self,username="",password="",email=""):
		self.response.write(user_signup_form % ({"username":username,"password":password,"email":email}))
	def get(self):
		self.write_form()
	def post(self):
		username = self.request.get("username")
		password = self.request.get("password")
		verify = self.request.get("verify")
		email = self.request.get("email")


	def welcome_message(self,username):
		self.response.out.write(welcome_message % ({"username": username}))


app = webapp2.WSGIApplication([('/', MainPage),('/unit2/rot13',Rot13),('/unit2/signup',Signup)], debug=True)
