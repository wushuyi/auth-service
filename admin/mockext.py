# -*- coding:utf-8 -*-
__author__ = 'wushuyi'
from flask import abort, redirect, url_for, request
from flask_admin import Admin, AdminIndexView, expose
from auth.model import User, Role, Client, Grant, Token
from flask_admin.contrib import mongoengine
from flask_security import login_required, current_user


class MyModelView(mongoengine.ModelView):
    def is_accessible(self):
        if not current_user.is_active() or not current_user.is_authenticated():
            return False

        if current_user.has_role('admin'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated():
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


class MyHomeView(AdminIndexView):
    @expose('/')
    def index(self):
        return 'Hello'


class UserView(MyModelView):
    pass


class RoleView(MyModelView):
    pass


class ClientView(MyModelView):
    pass


class GrantView(MyModelView):
    pass


class TokenView(MyModelView):
    pass


def setup_app(app):
    admin = Admin(app, name='auth admin', template_mode='bootstrap3')
    admin.add_view(UserView(User))
    admin.add_view(RoleView(Role))
    admin.add_view(ClientView(Client))
    admin.add_view(GrantView(Grant))
    admin.add_view(TokenView(Token))
