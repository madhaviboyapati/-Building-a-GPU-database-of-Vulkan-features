import webapp2
import jinja2
import os

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True
)

class GpuListPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'


        template = JINJA_ENVIRONMENT.get_template('GPU.html')
        self.response.write(template.render({}))

    def post(self):
        self.response.headers['Content-Type'] = 'text/html'

        template = JINJA_ENVIRONMENT.get_template('GPU.html')
        self.response.write(template.render({}))


app = webapp2.WSGIApplication([
    ('/gpu', GpuListPage),
], debug=True)