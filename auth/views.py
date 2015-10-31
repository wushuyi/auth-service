# -*- coding:utf-8 -*-
__author__ = 'wushuyi'
from flask import Blueprint, render_template, url_for, flash, get_flashed_messages, request, session, redirect, jsonify
from flask_security import Security, MongoEngineUserDatastore, login_required, current_user
from .public import app, db, oauth
from .model import Role, User, Client, Grant, Token
from .config import security_messages
from werkzeug.security import gen_salt
from datetime import datetime, timedelta

blueprint = Blueprint(
    'auth',
    __name__,
    static_url_path='/auth/static',
    static_folder='static',
    template_folder='templates'
)


def SetSecurityMessagesConfig(app, messages):
    for key, value in messages.items():
        app.config['SECURITY_MSG_' + key] = value

    return app


def getCurrUserModel(curruser):
    return User.objects(id=curruser.id).first()


user_datastore = MongoEngineUserDatastore(db, User, Role)
SetSecurityMessagesConfig(app, security_messages)
security = Security(app, user_datastore)


@blueprint.route("/", methods=['GET', ])
@login_required
def index():
    return current_user.email


@blueprint.route('/client')
@login_required
def client():
    item = Client(
        client_id=gen_salt(40),
        client_secret=gen_salt(50),
        _redirect_uris=' '.join([
            'http://localhost:8000/authorized',
            'http://127.0.0.1:8000/authorized',
            'http://127.0.1:8000/authorized',
            'http://127.1:8000/authorized',
        ]),
        _default_scopes='email',
        user=User.objects(id=current_user.id).first()
    )
    item.save()
    return jsonify(
        client_id=item.client_id,
        client_secret=item.client_secret,
    )


@oauth.clientgetter
def load_client(client_id):
    return Client.objects(client_id=client_id).first()


@oauth.grantgetter
def load_grant(client_id, code):
    curr_client = Client.objects(client_id=client_id).first()
    return Grant.objects(client=curr_client, code=code).first()


@oauth.grantsetter
def save_grant(client_id, code, request, *args, **kwargs):
    # decide the expires time yourself
    expires = datetime.utcnow() + timedelta(seconds=100)
    grant = Grant(
        client=Client.objects(client_id=client_id).first(),
        code=code['code'],
        redirect_uri=request.redirect_uri,
        _scopes=' '.join(request.scopes),
        user=getCurrUserModel(current_user),
        expires=expires
    )
    grant.save()
    return grant


@oauth.tokengetter
def load_token(access_token=None, refresh_token=None):
    if access_token:
        return Token.objects(access_token=access_token).first()
    elif refresh_token:
        return Token.objects(refresh_token=refresh_token).first()


@oauth.tokensetter
def save_token(token, request, *args, **kwargs):
    curr_client = Client.objects(client_id=request.client.client_id).first()
    curr_user = User.objects(id=request.user.id).first()
    toks = Token.objects(
        client=curr_client,
        user=curr_user
    )
    for t in toks:
        t.delete()

    expires_in = token.pop('expires_in')
    expires = datetime.utcnow() + timedelta(seconds=expires_in)

    tok = Token(
        access_token=token['access_token'],
        refresh_token=token['refresh_token'],
        token_type=token['token_type'],
        _scopes=token['scope'],
        expires=expires,
        client=curr_client,
        user=curr_user
    )
    tok.save()

    return tok


@blueprint.route('/oauth/token', methods=['GET', 'POST'])
@oauth.token_handler
def access_token():
    return None


@blueprint.route('/oauth/authorize', methods=['GET', 'POST'])
@login_required
@oauth.authorize_handler
def authorize(*args, **kwargs):
    if request.method == 'GET':
        client_id = kwargs.get('client_id')
        curr_client = Client.objects(client_id=client_id).first()
        curr_user = getCurrUserModel(current_user)
        kwargs['client'] = curr_client
        kwargs['user'] = curr_user
        return render_template('authorize.html', **kwargs)

    confirm = request.form.get('confirm', 'no')
    return confirm == 'yes'


@blueprint.route('/api/me')
@oauth.require_oauth()
def me():
    user = request.oauth.user
    return jsonify(email=user.email)


@blueprint.route("/flashed", methods=['GET', ])
def flashed():
    info = ''
    flash('hello')
    messages = get_flashed_messages(with_categories=True)
    if messages:
        for category, message in messages:
            print(message)
            info += message
    return info
