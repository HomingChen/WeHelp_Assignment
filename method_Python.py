# # 【要求一】
# print("【要求一】")
# def calculate(min, max, step):
#     result = 0
#     for i in range(min, max+1, step):
#         result += i
#     print(result)
# calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
# calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
# calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

# # 【要求二】
# print("【要求二】")
# def avg(data):
#     # 請用你的程式補完這個函式的區塊
#     item = len(data["employees"])
#     count = 0
#     sumSalary = 0
#     for i in range(item):
#         if data["employees"][i]["manager"]==False:
#             count += 1
#             sumSalary += data["employees"][i]["salary"]
#     else:
#         result = sumSalary / count
#         print(result)
# avg({
#     "employees":[
#         {
#             "name":"John",
#             "salary":30000,
#             "manager":False
#         },
#         {
#             "name":"Bob",
#             "salary":60000,
#             "manager":True
#         },
#         {
#             "name":"Jenny",
#             "salary":50000,
#             "manager":False
#         },
#         {
#             "name":"Tony",
#             "salary":40000,
#             "manager":False
#         }
#     ]
# }) # 呼叫 avg 函式

# 【要求三】
print("【要求三】")
def func(a):
    # 請用你的程式補完這個函式的區塊
    
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果
