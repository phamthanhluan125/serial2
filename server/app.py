import flask
import json
from flask import Flask, make_response, request, session
from datetime import timedelta
from config import Response

app = Flask(__name__, static_folder="../front/dist/front", static_url_path="")
app.secret_key = "abc!@#"

list_users = [
  {'id': 1, 'name': 'Nguyen Van A', 'sex': 'Male', 'age': 20, 'email': 'mail_a@gmail.com', 'password': '12345'},
  {'id': 2, 'name': 'Hoang Anh B', 'sex': 'Male', 'age': 28, 'email': 'mail_b@gmail.com', 'password': '12345'},
  {'id': 3, 'name': 'Nguyen Thi C', 'sex': 'Female', 'age': 31, 'email': 'mail_c@gmail.com', 'password': '12345'},
  {'id': 4, 'name': 'Pham Thanh D', 'sex': 'Male', 'age': 22, 'email': 'mail_d@gmail.com', 'password': '12345'}
]

limit_for_authentication = [
  'all_users',
  'add_user',
  'update_user',
  'delete_user'
]

@app.before_request
def before_request():
  session.permanent = True
  app.permanent_session_lifetime = timedelta(minutes=10)
  print session
  if 'logged_in' not in session and request.endpoint in limit_for_authentication:
    response = Response()
    response.create(Response.NOT_AUTHENTICATION)
    return flask.jsonify(json.dumps(response.__dict__))

@app.route('/')
def hello_world():
  return "Hello world."

@app.route('/users')
@app.route('/home')
@app.route('/login')
def response_pages():
  return make_response(open('../front/dist/front/index.html').read())


@app.route('/api/all_users')
def all_users():
  response = Response()
  response.create(Response.SUCCESS)
  response.data = list_users
  return flask.jsonify(json.dumps(response.__dict__))


@app.route('/api/add_user', methods=['POST'])
def add_user():
  response = Response()
  params = json.loads(request.data)
  if check_index(params['id']):
    response.create(Response.ERROR)
    response.data = 'Id have exist.'
  else:
    list_users.append(params)
    response.create(Response.SUCCESS)
    response.data = 'Created user.'
  return flask.jsonify(json.dumps(response.__dict__))

@app.route('/api/update_user', methods=['POST'])
def update_user():
  response = Response()
  params = json.loads(request.data)
  for user in list_users:
    if user['id'] == params['id']:
      user['name'] = params['name']
      user['age'] = params['age']
      user['sex'] = params['sex']
      user['email'] = params['email']
      break
  response.create(Response.SUCCESS)
  response.data = 'Update success.'
  return flask.jsonify(json.dumps(response.__dict__))

@app.route('/api/delete_user', methods=['POST'])
def delete_user():
  params = json.loads(request.data)
  del list_users[check_index(params['id'])]
  response = Response()
  response.create(Response.SUCCESS)
  response.data = 'Delete success.'
  return flask.jsonify(json.dumps(response.__dict__))

@app.route('/api/login', methods=['POST'])
def login():
  response = Response()
  params = json.loads(request.data)
  indexOfUser = check_index(params['email'], 'email')
  if indexOfUser >= 0 and list_users[indexOfUser]['password'] == params['password']:
    session['logged_in'] = True
    session['user_id'] = list_users[indexOfUser]['id']
    response.create(Response.SUCCESS)
    user = list_users[indexOfUser]
    user.pop('password', None)
    response.data = {'user': user}
  else:
    response.create(Response.NOT_FOUND)
  return flask.jsonify(json.dumps(response.__dict__))

@app.route('/api/logout')
def logout():
  response = Response()
  session.pop('logged_in', None)
  session.pop('user_id', None)
  response.create(Response.SUCCESS)
  return flask.jsonify(json.dumps(response.__dict__))


def check_index(id, key='id'):
  for index, user in enumerate(list_users):
    if user[key] == id:
      return index
  return False;

if __name__ == '__main__':
  app.run()
