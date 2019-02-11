from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect,url_for,request

class MyView(ModelView):
    can_create = False
    can_edit = False
    column_exclude_list = ['password_hash']

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        """redirect to login page if user doesn't have access"""
        return redirect(url_for('login', next=request.url))

class UserView(ModelView):
    can_create = False
    can_edit = False
    column_exclude_list = ['password_hash','role']

    def is_accessible(self):
        return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        """redirect to login page if user doesn't have access"""
        return redirect(url_for('login', next=request.url))