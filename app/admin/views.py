# from wtforms.fields import SelectField
from flask_admin import expose, BaseView
from flask_admin.contrib.sqla import ModelView


class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


class AdminUserView(ModelView):
    can_create = False
    can_edit = False
    column_exclude_list = ['password_hash']


class UserView(ModelView):
    can_create = False
    can_edit = False
    # column_exclude_list = ['password_hash','role']

