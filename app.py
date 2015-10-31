# -*- coding:utf-8 -*-
__author__ = 'wushuyi'
from gevent import monkey

monkey.patch_socket()
import os
from flask import Flask, send_from_directory
from flask_registry import Registry, PackageRegistry
from flask_registry import ExtensionRegistry
from flask_registry import ConfigurationRegistry
from flask_registry import BlueprintAutoDiscoveryRegistry
import config


def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


def create_app(config):
    app = Flask('myapp')
    app.config.from_object(config)
    r = Registry(app=app)
    r['packages'] = PackageRegistry(app)
    r['extensions'] = ExtensionRegistry(app)
    r['config'] = ConfigurationRegistry(app)
    r['blueprints'] = BlueprintAutoDiscoveryRegistry(app=app)

    app.add_url_rule('/favicon.ico', 'favicon', favicon)

    return app


if __name__ == '__main__':
    app = create_app(config)
    app.run(host='0.0.0.0', port=8080)
