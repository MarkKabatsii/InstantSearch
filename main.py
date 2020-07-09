import webapp2
from heandlers import (
    MainPage,
    GetHandler,
    SetHandler,
    UnsetHandler,
    NumEqualToHandler,
    UndoHandler,
    RedoHandler,
    EndHandler,
)


application = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/get', GetHandler),
    ('/set', SetHandler),
    ('/unset', UnsetHandler),
    ('/numequalto', NumEqualToHandler),
    ('/undo', UndoHandler),
    ('/redo', RedoHandler),
    ('/end', EndHandler)
], debug=False)
