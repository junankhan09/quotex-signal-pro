from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime, timedelta
import random
import secrets

# Get the absolute path to templates folder
import os
template_dir = os.path.abspath('templates')

app = Flask(__name__, template_folder=template_dir)
app.config['PASSWORD'] = os.environ.get('SITE_PASSWORD', 'jummuubot')
app.config['SECRET_KEY'] = secrets.token_hex(32)

# Add this test route
@app.route('/api/test')
def test():
    return jsonify({'status': 'ok', 'message': 'Server is running!'})