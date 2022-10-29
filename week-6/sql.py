from multiprocessing import parent_process
import mysql.connector              # 連接MySQL資料庫
from collections import namedtuple  # MySQL傳回的資料型態為tuple(即table的每一row)組合而成的list；利用namedtuple將tuple內的每個元素給予對應名稱(類似dictionary)，避免資料庫異動而有問題

websiteDB = mysql.connector.connect(host="localhost", user="root", password="7895123", database="website")
cursor = websiteDB.cursor()         # cursor: 類似暫存檔，在隨著執行各種查詢或輸入資料時，會將結果暫存於此

def login(username, password):
  queryStr = "SELECT * FROM member WHERE username=%(username)s;"
  cursor.execute(queryStr, params={'username': username})
  try:
    result = cursor.fetchone()
    memberData = namedtuple("memberData", cursor.column_names)._make(result)._asdict()
    if memberData["username"]==username and memberData["password"]==password:
      memberData["userStatus"] = "已登入"
      del memberData["password"]
    else:
      memberData = {"userStatus": "帳號、或密碼輸入錯誤"}
  except:
    memberData = {"userStatus": "帳號、或密碼輸入錯誤"}
  return memberData

def signup(name, username, password):
  if len(name)*len(username)*len(password)==0:
    return "請勿輸入空白資料"
  else:
    queryStr = "SELECT username FROM member WHERE username=%(username)s;"
    cursor.execute(queryStr, params={"username": username})
    if len(cursor.fetchall())==0:
      inputStr = "INSERT INTO member(name, username, password) VALUE (%s, %s, %s);"
      cursor.execute(inputStr, params=(name, username, password))
      websiteDB.commit()
      return "註冊成功"
    else:
      return "帳號已經被註冊"

def sendMessage(member_id=0, content=""):
  if member_id!=0 and len(content)>0:
    inputStr = "INSERT INTO message(member_id, content) VALUE (%s, %s);"  # MySQL以%s接收%i或%d，也不用刻意補'符號
    cursor.execute(inputStr, params=(member_id, content))
    websiteDB.commit()
    print("送出成功")
  else:
    print("未送出")

def getMessages():
  queryStr = """
             SELECT message.id, member.name, message.content, message.like_count, message.time
              FROM message INNER JOIN member ON message.member_id=member.id ORDER BY time;;
             """
  cursor.execute(queryStr, params=None)
  queryResult = cursor.fetchall()
  messages = []
  for i in queryResult:
    message = namedtuple("message", cursor.column_names)._make(i)._asdict()
    messages.append(message)
  return messages



# """
# 這裡是筆記區
# nametuple的筆記
# 1. 官方說明: https://docs.python.org/3/library/collections.html#collections.namedtuple
# 2. 概念: 製作一個函式,裡面架構好tuple內每個元素所對應的名字, 再把元素放入到此函式中, 完成後可以類似字典方式使用
# 3. 函式說明 - namedtuple(typename="tuple的名字", field_names="tuple內每個元素對應到的名字")
# 4. 函式說明 - someNamedTuple._make(iterable data): 把現有的有序資料(tuple, list, sequence...)放入已建立好的namedtuple函式中
# 5. 取用方式(tuple): tuple的名字.元素名字 = 對應元素的值
# 6. 函式說明 - someNamedTuple._asdict(): 把有名字的tuple格式改為dictionary，方便轉換為json
# 7. 取用方式(dictionary): dictionary的名字['元素名稱'] = 對應元素的值
# """ 