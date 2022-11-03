import sql, json
from flask import Flask, render_template, request, session, redirect,jsonify

app = Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key="welovepengpeng"
app.config['JSON_AS_ASCII'] = False                 # 讓utf-8正常顯示
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True    # 回傳漂亮的json格式

@app.route("/")
def index():
    session["userStatus"]="未登入"
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    result = sql.login(username, password)
    if result["loginResult"]=="登入成功":
        session["userStatus"] = "已登入"
        session["data"] = result["memberData"]
        return redirect("/member")
    else:
        return redirect("/error?message="+result["loginResult"])

@app.route("/api/member", methods=["GET", "PATCH"])
def memberData():
    if request.method=="GET":
        username = request.args.get("username","")
        if session["userStatus"]=="已登入" and len(username)>0:
            result = sql.searchName(username=username)
            return jsonify(result)
        else:
            return jsonify({"data": "null"})
    elif request.method=="PATCH":
        newName = request.get_json()
        result = sql.updateName(newName=newName["name"], id=session["data"]["id"])
        if result.get("ok")=="true": 
            session["data"]["name"] = newName
        else: 
            pass
        return jsonify(result)

@app.route("/member")
def member():
    if session["userStatus"]=="已登入":
        name = session["data"]["name"]
        return render_template("member.html", name=name)
    else:
        return redirect("/")

@app.route("/error")
def error():
    message = request.args.get("message","自訂的錯誤訊息")
    return render_template("error.html", data=message)

@app.route("/signout")
def signout():
    session["userStatus"] = "未登入"
    return render_template("signout.html")

app.run(port=3000)
