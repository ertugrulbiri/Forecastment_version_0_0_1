# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import os
from flask import request, jsonify
from app import create_app
from config.config import Config
app = create_app(Config)

if __name__ == '__main__':
    app.run(host='0.0.0.0')

