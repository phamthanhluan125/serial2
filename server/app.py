import flask
import json
from flask import Flask, make_response, request
from config import Response

app = Flask(__name__, static_folder="../front/dist/front", static_url_path="")
list_users = [
  {'id': 1, 'name': 'Nguyen Van A', 'sex': 'Male', 'age': 20, 'email': 'mail_a@gmail.com'},
  {'id': 2, 'name': 'Hoang Anh B', 'sex': 'Male', 'age': 28, 'email': 'mail_b@gmail.com'},
  {'id': 3, 'name': 'Nguyen Thi C', 'sex': 'Female', 'age': 31, 'email': 'mail_c@gmail.com'},
  {'id': 4, 'name': 'Pham Thanh D', 'sex': 'Male', 'age': 22, 'email': 'mail_d@gmail.com'}
]
@app.route('/')
def hello_world():
  return "Hello world."

@app.route('/users')
@app.route('/home')
def home():
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

def check_index(id):
  for index, user in enumerate(list_users):
    if user['id'] == id:
      return index
  return False;

if __name__ == '__main__':
  app.run()
