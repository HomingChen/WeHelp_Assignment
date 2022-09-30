text = """
Q1：時間複雜度 (Time Complexity) 的概念，試著讓自己用幾句話回答什麼是時間複雜度?\n
    定義：在電腦科學領域當中，時間複雜度用來描述一段程式(更精確地說是演算法)最大會執行的時間。\n
          當時間複雜度的值越大，表示需要越久的時間來完成執行。\n
    目的：時間複雜度可做為衡量演算法的效能指標(之一?)。例如有種方法可以讓我從高雄到台北(高鐵、\n
          台鐵、客運、計程車…)，在同樣的結果(抵達台北)之下，由於高鐵的行駛速度較快、所需時間較\n
          小，其效能就比搭計程車還要高(在不考慮沒有地震停駛的情況)。所以，時間複雜度的值越大，\n
          表示需要越久的時間來完成執行，其效能也就越低。\n
    表達方式：時間複雜度通常會以俗稱的大O符號來表達，數學運算上以O呈現：(1) 此處的O要念作\n
          Omicron，跟covid-19的Omicron一樣是借用希臘字母。(2) 統整為O(1)、O(n)、O(logn^2)\n
          等，以下題做詳盡的說明。\n\n
Q2：分析一下你自己寫的程式，每一題解法的時間複雜度若以 Big-O Notation 來表達，時間複雜度是？
"""
print(text)
# 【要求一】
print("【要求一】：O(n), n=1+(max-min)/step，n會依照參數而有不同")
def calculate(min, max, step):
    result = 0
    for i in range(min, max+1, step):
        result += i
    print(result)
    return result
calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

# 【要求二】
print("【要求二】：O(n), n=employees內資料的筆數，n會依照參數而有不同")
def avg(data):
    # 請用你的程式補完這個函式的區塊
    item = len(data["employees"])
    count = 0
    sumSalary = 0
    for i in range(item):
        if data["employees"][i]["manager"]==False:
            count += 1
            sumSalary += data["employees"][i]["salary"]
    else:
        result = sumSalary / count
        print(result)
        return result
avg({
    "employees":[
        {
            "name":"John",
            "salary":30000,
            "manager":False
        },
        {
            "name":"Bob",
            "salary":60000,
            "manager":True
        },
        {
            "name":"Jenny",
            "salary":50000,
            "manager":False
        },
        {
            "name":"Tony",
            "salary":40000,
            "manager":False
        }
    ]
}) # 呼叫 avg 函式

# 【要求三】
print("【要求三】：O(2), 因為curried的關係，會先進行a的運算，再執行(b, c)，且無論a,b,c的參數，皆固定為2")
def func(a):
    def funcCaculate(b,c):
        result = a + b * c
        print(result)
        return result
    return funcCaculate
func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

# 【要求四】
print("【要求四】：O(n^2), n=n(n-1)/2, 泡沫排序")
def maxProduct(nums):
    item = len(nums)
    arrayProduct = []
    for i in range(item):
        for j in range(i+1, item):
            result = nums[i] * nums[j]
            arrayProduct = arrayProduct + [result]
    maxProductResult = max(arrayProduct)
    print(maxProductResult)
    return maxProductResult
maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10

# 【要求五】
print("【要求五】：O(n^2), n=n(n-1)/2, 泡沫排序")
def twoSum(nums, target):
    item = len(nums)
    for i in range(item):
        for j in range(i+1, item):
            if nums[i]+nums[j]==target:
                sumResult = f"[{i}, {j}]"
                return sumResult
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

# 【要求六】
print("【要求六】：O(n), n=set的長度")
def maxZeros(nums):
    nums = nums+[1]
    item = len(nums)
    len_0 = 0
    arrayLen_0 = [0]
    for i in range(item):
        if nums[i]==0:
            len_0 += 1
        elif nums[i]!=0 and len_0>0:
            arrayLen_0 = arrayLen_0 + [len_0]
            len_0 = 0
    result = max(arrayLen_0)
    print(result)
    return result
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3