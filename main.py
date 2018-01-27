# main.py

import webapp2
from content import CONTENT

class Home(webapp2.RequestHandler):
    def get(self):
        
        # Create links to the Login handler.
        self.response.write(CONTENT)


# Create routes.
ROUTES = [webapp2.Route(r'/', Home)]

# Instantiate the webapp2 WSGI application.
app = webapp2.WSGIApplication(ROUTES, debug=True)
