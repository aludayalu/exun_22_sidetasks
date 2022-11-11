import pickle,uuid,base64
from flask import Flask,make_response,request,send_file
app=Flask(__name__)

style="""
<style>
body {
    background-image: linear-gradient(to left bottom, #072e69, #253790, #503bb5, #8335d3, #bc12eb);
}
p {
    font-size: large;
    text-align: center;
    margin-top: 20%;
}
</style>
"""

class test:
    def __init__(self,id) -> None:
        self.id=id

def base(id):
    return style+f"<p>Hello user {id}!<br>Welcome to our site.<br>This site is currently in development.<!--3taTLNS--><p>"

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

app.run(port=5000)