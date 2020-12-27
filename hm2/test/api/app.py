import random
import os
import re

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from string import Template
import pandas as pd
import psycopg2

HTML_TEMPLATE = Template("""
<form method="POST">
    <input name="variable">
    <input type="submit">
</form>
<iframe width="1280" height="720" src="https://www.youtube.com/embed/${youtube_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
""")

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

def send_sql_query(query):
    params = {
        'database': 'songlist',
        'host': '172.17.0.2',
        'user': 'postgres',
        'password': 'postgres',
    }
    try:
        conn = psycopg2.connect(**params)
    except:
        params['host'] = '172.17.0.3'
        conn = psycopg2.connect(**params)
    raw_data = pd.read_sql_query(query, conn)
    conn.close()
    return raw_data


def get_links():
    return send_sql_query(
       """
       SELECT link FROM links
       """
    )['link'].to_list()
    
def add_links(link, link_id):
    link = re.search('(?<=watch\?v=).*', link).group()
    params = {
        'database': 'songlist',
        'host': '172.17.0.2',
        'user': 'postgres',
        'password': 'postgres',
    }
    try:
        conn = psycopg2.connect(**params)
    except:
        params['host'] = '172.17.0.3'
        conn = psycopg2.connect(**params)
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO links (link_id, link) VALUES({link_id}, '{link}')")
    conn.commit()
    cursor.close()
    conn.close()
    return link

@app.route('/')
def homepage():
    links = set(get_links())
    vid = random.choice(list(links))
    return HTML_TEMPLATE.substitute(youtube_id=vid)

@app.route('/', methods=['POST'])
def my_form_post():
    variable = request.form['variable']
    links = get_links()
    new_link = add_links(variable, len(links) + 1)
    vid = random.choice(links + [new_link])
    return HTML_TEMPLATE.substitute(youtube_id=vid)

@app.route('/videos/<vid>')
def videos(vid):
    return HTML_TEMPLATE.substitute(youtube_id=random.choice(links))

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=80, debug=True, host='0.0.0.0')



