from flask import Flask
app = Flask(__name__)
 
@app.route('/')
def hello_world():
   return 'Launch successful.'
 
if __name__ == '__main__':
   app.run(port=80, debug=True, host='0.0.0.0')
