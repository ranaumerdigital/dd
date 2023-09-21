from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This is homepage"

@app.route('/index')
def iN():
    return "This is index page"

if __name__== "__main__":
   app.run(debug=True)