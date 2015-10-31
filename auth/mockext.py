# -*- coding:utf-8 -*-
__author__ = 'wushuyi'
from flask_mongoengine import MongoEngine
from flask_mail import Mail
from flask_oauthlib.provider import OAuth2Provider
import auth.public as public
from .config import MockConfig


def setup_app(app):
    config = MockConfig()
    app.config.from_object(config)
    db = app.extensions.get('mongoengine')
    if not db:
        db = MongoEngine(app)
    mail = app.extensions.get('mail')
    if not mail:
        mail = Mail(app)
    oauth = app.extensions.get('oauthlib.provider.oauth2')
    if not oauth:
        oauth = OAuth2Provider(app)
    public.app = app
    public.db = db
    public.mail = mail
    public.oauth = oauth
