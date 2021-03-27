from flask import Flask,request
from backend.Util.token import create_token, validate_token
from backend.Database.database import Data
import json

app = Flask(__name__)
data = Data()

@app.route('/front',methods="GET")
def index():
    return

@app.route('/backend',methods="GET")
def index():
    return

@app.route('/api/user/meeting',methods="GET")
def message():
    return

@app.route('/api/user/forum/message',methods="POST")
def message():
    token = request.form.get("token")
    user_id,msg = validate_token(token)
    user_id = user_id["user_id"]
    page = request.form.get("page")
    id = request.form.get("id")
    if id is None:
        return
    return

@app.route('/api/user/query/follow',methods="POST")
def ask_follow():
    token = request.form.get("token")
    user_id,msg = validate_token(token)
    user_id = user_id["user_id"]
    id = request.form.get("id")
    return

@app.route('/api/user/forum/list',methods="POST")
def forum_list():
    token = request.form.get("token")
    user_id,msg = validate_token(token)
    user_id = user_id["user_id"]
    return

@app.route('/api/user/follow/',methods="POST")
def follow():
    token = request.form.get("token")
    user_id,msg = validate_token(token)
    user_id = user_id["user_id"]
    follow_key = request.form.get("follow_key")
    ids = request.form.get("ids")
    for id in ids:
        if follow_key == 1:
            data.is_like(user_id,id)
        else:
            data.like(user_id,id)
    rex = {
        "error_code":0
    }
    return json.dumps(rex)

@app.route('/api/user/register',methods="POST")
def register():
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")
    return

@app.route('/api/user/login',methods="POST")
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    result = data.get_user(email,password)
    if result is None:
        rex = {
            "error_code":1
        }
        return json.dumps(rex)
    token = create_token(result[0])
    username = result[4]
    first = result[5]
    rex = {
        "error_code":0,
        "data":{
            "token":token,
            "username":username,
            "first": first
        }
    }
    return json.dumps(rex)

@app.route('/api/admin/login',methods="POST")
def login():
    email = request.form.get("email")
    password = request.form.get("password")
    return

@app.route('/api/admin/stastic',methods="POST")
def static():
    token = request.form.get("token")
    user_id,msg = validate_token(token)
    user_id = user_id["user_id"]
    return

@app.route('/api/admin/getParticipant',methods="POST")
def getpatica():
    token = request.form.get("token")
    user_id,msg = validate_token(token)
    user_id = user_id["user_id"]
    page = request.form.get("page")
    return

@app.route('/api/admin/publish',methods="POST")
def podcast():
    id = request.form.get("id")
    content = request.form.get("content")
    token = request.form.get("token")
    user_id,msg = validate_token(token)
    user_id = user_id["user_id"]
    return

@app.route('/api/admin/forums',methods="POST")
def forums():
    token = request.form.get("token")
    user_id,msg = validate_token(token)
    user_id = user_id["user_id"]
    return

@app.route('/api/user/query/follow',methods="POST")
def queryf():
    id = request.form.get("id")
    token = request.form.get("token")
    user_id = validate_token(token)["user_id"]
    rex = {
        "error_code":0,
        "data":{
            "follow":data.is_followed(user_id,id)
        }
    }
    return json.dumps(rex)



if __name__ == '__main__':
    app.run()
