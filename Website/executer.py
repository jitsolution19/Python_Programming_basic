from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('index.html')

# @app.route('/')
# def index():
#    return '<html><body><h1>Hello World</h1></body></html>'

if __name__ == '__main__':
   app.run(debug = True)