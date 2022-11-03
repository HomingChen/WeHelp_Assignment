import mysql.connector
from collections import namedtuple

websiteDB = mysql.connector.connect(host="localhost", user="root", password="7895123", database="website")
cursor = websiteDB.cursor()

def login(username, password):
  queryStr = "SELECT id, name, username, password FROM member WHERE username=%(username)s;"
  cursor.execute(queryStr, params={'username': username})
  try:
    result = cursor.fetchone()
    memberData = namedtuple("memberData", cursor.column_names)._make(result)._asdict()
    if memberData["username"]==username and memberData["password"]==password:
      loginResult = "登入成功"
      del memberData["password"]
    else:
      memberData = "null"
      loginResult = "帳號、或密碼輸入錯誤"
  except:
    memberData = "null"
    loginResult = "帳號、或密碼輸入錯誤"
  return {"loginResult": loginResult, "memberData": memberData}

def searchName(username):
  queryStr = "SELECT id, name, username FROM member WHERE username=%(username)s;"
  cursor.execute(queryStr, params={"username": username})
  result = cursor.fetchone()
  if result==None:
    return {"data": "null"}
  else:
    searchData = namedtuple("message", cursor.column_names)._make(result)._asdict()
    return {"data": searchData}

def updateName(newName, id):
  queryStr = "UPDATE member SET name=%s WHERE id=%s;"
  try:
    cursor.execute(queryStr, params=(newName, id))
    websiteDB.commit()
    return {"ok": "true"}
  except:
    return {"error": "true"}
