# -*- coding:utf-8 -*-
__author__ = 'wushuyi'
from flask_security import UserMixin, RoleMixin
from .public import db


class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

    def __str__(self):
        return self.name


class User(db.Document, UserMixin):
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

    def __str__(self):
        return self.email


class Client(db.Document):
    client_id = db.StringField(max_length=40)
    client_secret = db.StringField(max_length=55)

    user = db.ReferenceField('User')

    _redirect_uris = db.StringField()
    _default_scopes = db.StringField()

    @property
    def client_type(self):
        return 'public'

    @property
    def redirect_uris(self):
        if self._redirect_uris:
            return self._redirect_uris.split()
        return []

    @property
    def default_redirect_uri(self):
        return self.redirect_uris[0]

    @property
    def default_scopes(self):
        if self._default_scopes:
            return self._default_scopes.split()
        return []


class Grant(db.Document):
    user = db.ReferenceField(User)

    client = db.ReferenceField(Client)

    code = db.StringField()

    redirect_uri = db.StringField(max_length=225)
    expires = db.DateTimeField()

    _scopes = db.StringField()

    @property
    def scopes(self):
        if self._scopes:
            return self._scopes.split()
        return []


class Token(db.Document):
    client = db.ReferenceField(Client)

    user = db.ReferenceField(User)

    token_type = db.StringField(max_length=40)

    access_token = db.StringField(max_length=255)
    refresh_token = db.StringField(max_length=255)
    expires = db.DateTimeField()
    _scopes = db.StringField()

    @property
    def scopes(self):
        if self._scopes:
            return self._scopes.split()
        return []
