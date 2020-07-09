import webapp2
from google.appengine.ext import db


STACKUNDO = []
STACKREDO = []
HTML = """<html><body>%s</body></html>"""


class DataSet(db.Model):
    name = db.StringProperty()
    value = db.StringProperty()


class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write('<h1>Hello world!</h1>')


class SetHandler(webapp2.RequestHandler):
    def get(self):
        variable_name = self.request.get('name')
        variable_value = self.request.get('value')
        data_key = db.Key.from_path('DataSet', variable_name)
        data_var = db.get(data_key)
        if data_var is None:
            STACKUNDO.append((variable_name, "None"))
        STACKUNDO.append((variable_name, variable_value))
        key = db.Key.from_path('DataSet', 'a')
        variable = db.get(key)
        comment = DataSet(
            name=variable_name,
            value=variable_value,
            key_name=variable_name,
        )
        comment.put()
        if variable is not None and variable.name == variable_name:
            self.response.write('<p></p>')
        else:
            self.response.write('<p>%s=%s</p>' % (variable_name, variable_value))


class GetHandler(webapp2.RequestHandler):
    def get(self):
        variable_name = self.request.get('name')
        key = db.Key.from_path('DataSet', variable_name)
        variable = db.get(key)
        self.response.write('<p>%s</p>' % variable.value)


class UnsetHandler(webapp2.RequestHandler):
    def get(self):
        variable_name = self.request.get('name')
        comment = DataSet(
            name=variable_name,
            value='None',
            key_name=variable_name,
        )
        comment.put()
        STACKUNDO.append((variable_name, "None"))
        key = db.Key.from_path('DataSet', variable_name)
        variable = db.get(key)
        self.response.write('<p>%s=%s</p>' % (variable_name, variable.value))


class NumEqualToHandler(webapp2.RequestHandler):
    def get(self):
        query = DataSet.all().filter('value =', self.request.get('value'))
        count = 0
        for self.num in query:
            count += 1
        if count != 0:
            self.response.write('<p>%s</p>' % count)
        else:
            self.response.write('<p>%s</p>' % count)


class UndoHandler(webapp2.RequestHandler):
    def get(self):
        if not STACKUNDO:
            self.response.write('<p>NO COMMANDS</p>')
        if STACKUNDO:
            key, value = STACKUNDO.pop()
            STACKREDO.append((key, value))
            comment = DataSet(
                name=key,
                value=value,
                key_name=key,
            )
            comment.put()
            self.response.write('<p>%s=%s</p>' % (key, value))


class RedoHandler(webapp2.RequestHandler):
    def get(self):
        if not STACKREDO:
            self.response.write('<p>NO CAMMANDS</p>')
        if STACKREDO:
            key, value = STACKREDO.pop()
            comment = DataSet(
                name=key,
                value=value,
                key_name=key,
            )
            comment.put()
            self.response.write('<p>%s=%s</p>' % (key, value))


class EndHandler(webapp2.RequestHandler):
    def get(self):
        query = DataSet.all()
        entries = query.fetch(1000)
        db.delete(entries)
        STACKUNDO[:] = []
        self.response.write('<p>CLEANED</p>')

