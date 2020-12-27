from flask import Flask
from string import Template
import random
from favorite_list import links

HTML_TEMPLATE = Template("""
<iframe width="1280" height="720" src="https://www.youtube.com/embed/${youtube_id}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
""")

app = Flask(__name__)

@app.route('/')
def homepage():
    vid = random.choice(links)
    return HTML_TEMPLATE.substitute(youtube_id=vid)

@app.route('/videos/<vid>')
def videos(vid):
    return HTML_TEMPLATE.substitute(youtube_id=random.choice(links))

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=80, debug=False, host='0.0.0.0')



