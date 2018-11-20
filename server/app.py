from flask import Flask, make_response

app = Flask(__name__, static_folder="../front/dist/front", static_url_path="")

@app.route('/')
def hello_world():
  return "Hello world."

@app.route('/home')
def home():
  return make_response(open('../front/dist/front/index.html').read())

if __name__ == '__main__':
  app.run()
