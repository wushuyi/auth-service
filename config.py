# -*- coding:utf-8 -*-
PACKAGES = ['auth', 'admin']
EXTENSIONS = ['auth.mockext', 'admin.mockext']
DEBUG = True

SECRET_KEY = 'super-secret'
MONGODB_SETTINGS = {
    'db': 'mydatabase',
    'host': 'localhost',
    'port': 27017
}
