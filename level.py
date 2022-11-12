import pickle,uuid,base64
from flask import Flask,make_response,request,send_file
app=Flask(__name__)

style="""
<style>
body {
    background: #ebebeb;
    display: flex;
    width: 100%;
    height: 100vh;
    justify-content: center;
    align-items: center;
}
p {
    font-size: large;
    text-align: center;
}
</style>
"""

class test:
    def __init__(self,id) -> None:
        self.id=id

def base(id):
    return style+f"<div class=\"content\">Hello user {id}!<br>Welcome to our site.<br>This site is currently in development.<!--3taTLNS--></div>"

@app.route("/house.ogg")
def house():
    return send_file("house.ogg")

@app.route('/')
def home():
    if request.cookies.get("sessionid")==None:
        id=str(uuid.uuid4())
        resp=make_response(base(id))
        resp.set_cookie("sessionid",base64.b64encode(pickle.dumps(test(id))).decode())
        return resp
    try:
        return base(pickle.loads(base64.b64decode(request.cookies.get("sessionid").encode())).id)
    except:
        return base(pickle.loads(base64.b64decode(request.cookies.get("sessionid").encode())))

app.run(port=5000,debug=1)