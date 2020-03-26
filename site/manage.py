#!/usr/bin/env python
import os
from app import create_app
# from flask.ext.script import Manager # deprecated; there's a link I could cite, but forget it. 
from flask_script import Manager # updated

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__' : manager.run()