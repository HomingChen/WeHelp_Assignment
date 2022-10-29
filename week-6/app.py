import sql, json
from flask import Flask, render_template, request, session, redirect

app = Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key="welovepengpeng"

@app.route("/")
def index():
    if session["userStatus"]!="新註冊":
        return render_template("index.html", newbie="未登入")
    else:
        return render_template("index.html", newbie="新註冊")

@app.route("/signin", methods=["POST"])
def signin():
    username = request.form["username"]
    password = request.form["password"]
    session["userStatus"] = "未登入"
    result = sql.login(username, password)
    if result["userStatus"]=="已登入":
        session["userStatus"] = "已登入"
        session["memberData"] = result
        return redirect("/member")
    else:
        return redirect("/error?message="+result["userStatus"])

@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name_signup"]
    username = request.form["username_signup"]
    password = request.form["password_signup"]
    result = sql.signup(name, username, password)
    if result=="註冊成功":
        session["userStatus"] = "新註冊"
        return redirect("/")
    else:
        session["userStatus"] = "未登入"
        return redirect("/error?message="+result)

@app.route("/member")
def member():
    if session["userStatus"]=="已登入":
        name = session['memberData']['name']
        return render_template("member.html", name=name)
    else:
        return redirect("/")

@app.route("/getMessages", methods=["POST"])
def messages():
    if session["userStatus"]=="已登入":
        messages = sql.getMessages()
        return json.dumps(messages, ensure_ascii=False, default=str)
    else:
        return redirect("/")

@app.route("/sendMessage", methods=["POST"])
def sendMessage():
    newMessage = request.form["newMessage"]
    if len(newMessage)>0:
        sql.sendMessage(member_id=session["memberData"]["id"], content=newMessage)
        return redirect("/member")
    else:
        return redirect("/member")

@app.route("/error")
def error():
    message = request.args.get("message","自訂的錯誤訊息")
    return render_template("error.html", data=message)

@app.route("/signout")
def signout():
    session["userStatus"] = "未登入"
    return render_template("signout.html")

app.run(port=3000)

# """
# 這裡是筆記區
# json.dumps
# 1. dump和dumps的差異：其實大同小異，只是差別在於
# 2. 將中文資料json化的參數設定(ensure_ascii=False)：json解譯字串預設為ASCIII，如有非ASCIII編碼者，須將參數ensure_ascii改為False
# 3. 將時間資料json化的參數設定(default=str)：使用Pythonn索取MySQL的datetime格式資料，MySQL會傳回datetime.datetime(yyyy, MM, dd, hh, mm, ss)的時間格式，
#    而非易讀的字串(yyyy-MM-dd hh:mm:ss)格式；此情況也就法寫入以字串傳輸資料的json，所以設定default=str參數，其作用就是將時間格式改為字串
# """