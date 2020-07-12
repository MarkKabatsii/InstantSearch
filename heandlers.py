import webapp2
import jinja2
import os
from google.appengine.ext import db

jinja_environment = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__) + '/templates')
)

STACKUNDO = []
STACKREDO = []


class DataSet(db.Model):
    name = db.StringProperty()
    value = db.StringProperty()


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_vars = {
            'dates': ['Hello world!']
        }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_vars))


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
            self.response.write('')
        else:
            self.response.write(variable_name + '=' + variable_value)


class GetHandler(webapp2.RequestHandler):
    def get(self):
        variable_name = self.request.get('name')
        key = db.Key.from_path('DataSet', variable_name)
        variable = db.get(key)
        template_vars = {
            'dates': [variable.value]
        }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_vars))


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
        self.response.write(variable_name + "=" + variable.value)


class NumEqualToHandler(webapp2.RequestHandler):
    def get(self):
        query = DataSet.all().filter('value =', self.request.get('value'))
        count = 0

        for self.num in query:
            count += 1
        if count != 0:
            template_vars = {
                'dates': [count]
            }
        else:
            template_vars = {
                'dates': [count]
            }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(template_vars))


class UndoHandler(webapp2.RequestHandler):
    def get(self):
        if not STACKUNDO:
            self.response.write('NO COMMANDS')
        if STACKUNDO:
            key, value = STACKUNDO.pop()
            STACKREDO.append((key, value))
            comment = DataSet(
                name=key,
                value=value,
                key_name=key,
            )
            comment.put()
            self.response.write(key + '=' + value)


class RedoHandler(webapp2.RequestHandler):
    def get(self):
        if not STACKREDO:
            var_text = {
                'dates': ['NO COMMANDS'],
            }
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(var_text))
        if STACKREDO:
            key, value = STACKREDO.pop()
            comment = DataSet(
                name=key,
                value=value,
                key_name=key,
            )
            comment.put()
            var_data = [key, '=', value]
            var_text = {
                'dates': var_data,
            }
            template = jinja_environment.get_template('index.html')
            self.response.out.write(template.render(var_text))


class EndHandler(webapp2.RequestHandler):
    def get(self):
        query = DataSet.all()
        entries = query.fetch(1000)
        db.delete(entries)
        STACKUNDO[:] = []
        var_text = {
            'dates': 'CLEANED'
        }
        template = jinja_environment.get_template('index.html')
        self.response.out.write(template.render(var_text))
