from flask import Flask, render_template
from flask import url_for
import os

app = Flask(__name__)

@app.route('/static/')
def get_d3_data():
    return None

@app.route('/bar')
def render_bar():
    return render_template('bar.html')

@app.route('/states')
def render_states():
    return render_template('states.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
