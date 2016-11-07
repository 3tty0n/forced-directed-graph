# coding: utf-8

import os
from flask import Flask, render_template, url_for, redirect
from utils.util import create_json_from_file

app = Flask(__name__)
app.config['DEBUG'] = True


def generate_json(name):
    return {"name": name, "url": '/view/' + name, "generate_url": '/api/' + name}


@app.route('/')
def index():
    graph = list()
    graph.append(generate_json('twitter_combined'))
    graph.append(generate_json('com-amazon.ungraph'))
    graph.append(generate_json('BA10000'))
    return render_template('index.html',
                           title='Forced-Directed Layout',
                           subtitle='built with flask, NetworkX and D3.js.',
                           github='https://github.com/3tty0n/forced-directed-graph',
                           profile='https://github.com/3tty0n',
                           graphs=graph)


@app.route('/view/<filename>')
def render(filename):
    js_url = url_for('static', filename='forced.js')
    json_url = url_for('static', filename=filename + '.json')
    return render_template('forced_graph.html',
                           title=filename,
                           js_url=js_url,
                           graph_name=json_url)


@app.route('/api/<filename>')
def generate_graph(filename):
    js_url = url_for('static', filename='forced.js')
    json_url = url_for('static', filename=filename + '.json')

    if filename == 'twitter_combined':
        create_json_from_file(filename, 1000)
    else:
        create_json_from_file(filename, 3000)

    return render_template('forced_graph.html', title=filename, js_url=js_url, graph_name=json_url)

if __name__ == '__main__':
    print('\nGo to http://localhost:5000 to see the example\n')
    port = int(os.environ.get('PORT', 5000))
    app.run()
