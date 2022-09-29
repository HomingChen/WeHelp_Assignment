# 【要求一】
print("【要求一】")
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
print("【要求二】")
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
print("【要求三】")
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
print("【要求四】")
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
print("【要求五】")
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
print("【要求六】")
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