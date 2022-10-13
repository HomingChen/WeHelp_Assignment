from flask import Flask, render_template, request, session, redirect

app = Flask(__name__, static_folder="static", static_url_path="/")
app.secret_key="welovepengpeng"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin", methods=["POST"])
def signin():
    account = request.form["account"]
    password = request.form["password"]
    session["userStatus"] = "未登入"
    if account=="test" and password=="test":
        session["userStatus"] = "已登入"
        return redirect("/member")
    elif account=="" or password=="":
        return redirect("/error?message=請輸入帳號、密碼")
    else:
        return redirect("/error?message=帳號、或密碼輸入錯誤")

@app.route("/member")
def member():
    if session["userStatus"]=="已登入":
        return render_template("member.html")
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

@app.route("/calculate")
def calculate():
    inputNumber = request.args.get("inputNumber","notNumber")
    return redirect("/square/"+str(inputNumber))

@app.route("/square/<inputNumber>")
def square(inputNumber):
    try:
        if abs(float(inputNumber))/int(float(inputNumber))==1:
            result = int(float(inputNumber)) ** 2
            return render_template("square.html", data=result)
        else:
            return redirect("/error?message=輸入的值並非正整數")
    except ValueError:
        return redirect("/error?message=輸入的值並非正整數")

@app.route("/square/")
def squareError():
    return redirect("/error?message=請輸入正整數")

app.run(port=3000)