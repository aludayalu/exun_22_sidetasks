import flask
from flask import Flask,request
app=Flask(__name__)

@app.route("/auth",methods=["POST","GET"])
def auth():
    try:
        if getattr(__import__("details",fromlist=[request.form["nm"]]),request.form["nm"])==request.form["key"]:
            return f'Auth successful<br>Your password is {getattr(__import__("details",fromlist=[request.form["nm"]]),request.form["nm"])}'+" Exun{this_was_fun}"*int(request.form["nm"]=="exun_admin")
        else:
            return "Invalid Credentials"
        return 
    except:
        return "Invalid Credentials"

@app.route("/login")
def login():
    return """
<html>
   <body>
      <form action = "/auth" method = "POST">
         <p><h3>Enter userID</h3></p>
         <p><input type = 'text' name = 'nm'/></p>
         <p><h3>Enter Key</h3></p>
         <p><input type = 'password' name = 'key'/></p>
         <p><input type = 'submit' value = 'Login'/></p>
      </form>
   </body>
</html>
"""
@app.route("/people/<person>")
def author(person):
    return getattr(__import__("details",fromlist=[person]),person).replace(".",".<br>")
@app.route("/")
def home():
    return """
Welcome to my blog

Some famous people
<a href="/people/satoshi_nakamoto">Satoshi Nakamoto</a>
<a href="/people/vitalik_buterin">Vitalik Buterin</a>

Blog 1
<!--/3G5XXpJ--->
""".replace("\n","<br>")

@app.route("/robots.txt")
def code():
    return "<plaintext>"+open(__file__).read().replace("Exun{this_was_fun}","flag_here")+"</plaintext>"
app.run(port=7777)