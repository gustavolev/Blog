
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
    <form method="post">
      <input type="text" name="nome">
      <input type="submit">
    </form>
  </body>
</html>
      """
    )

  def post(self):
    nome = self.request.get("nome")
    self.response.out.write("Oi " + nome)

app = webapp2.WSGIApplication([
  ('/', MainHandler)
])