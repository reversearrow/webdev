from functions import rot13
import webapp2

rot13_form = """
<h2>Enter some Rot13 text here</h2>
<form method="POST">
<input type="text" name="text" value="%(text)s" style="height: 100px; width: 400px"></input><br>
<input type="submit">
</form>
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


app = webapp2.WSGIApplication([('/', MainPage),('/unit2/rot13',Rot13)], debug=True)
