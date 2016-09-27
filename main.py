
import webapp2

class MainHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(
      """
<html>
  <head>
    <title>Awesome Blog!</title>
  </head>
  <body>
    Essa e a pagina principal!
  </body>
</html>
      """
    )
  
  def post(self):
    numero = self.request.get("numero")
    self.response.out.write(int(numero)**2)

class LoginHandler(webapp2.RequestHandler):
  def get(self):
    self.response.out.write(
      """
<html>
  <head>
    <title>Awesome Blog!</title>
  </head>
  <body>
    Essa e a pagina de login!
  </body>
</html>
      """
    )

app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/login', LoginHandler)
])
