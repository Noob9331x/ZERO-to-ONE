# print("Hello, World!")


# money = 50
# ice = 10.5
# coke = 5
# # def buy():
# #     print(money - ice - coke)

# # buy()
# print(type(money))
# print(type(ice))
# print(type(int(ice)))
# print(int(ice))

#字符串拼接
# money = 10
# name = "小明"
# salary = 10000
# # print("我是" + name + ",我的工资发了" + str(money) + "元" + ",我钱包里还有" + str(salary))  # 字符串拼接

# print(f"我是{name},我的工资发了{money}元,我钱包里还有{salary}")  # f-string格式化输出

# 股价计算小程序
# name = "博客"
# stock_price = 6.5
# stock_code = "003032"
# stock_price_daily_growth_factor = 1.2
# growth_days = 7
# print(f"公司：{name},股票代码：{stock_code}, 当前股价：{stock_price}")
# print("每天增长系数：%.1f,经过%d天增长后，股价到达了：%.2f"
#  % (stock_price_daily_growth_factor, growth_days, stock_price * (stock_price_daily_growth_factor ** growth_days)))

# if 判断练习
# print(f"欢迎来到儿童游乐场，儿童免费，成人收费。")
# age = int(input("请输入你的年龄："))

# if age >= 18:
#     print("你是成人，需要购票入场！\n票价：50元")
# else:
#     print("你是儿童，可以免费入场！")
# print("欢迎来到儿童游乐场")
# height = float(input("请输入你的身高（单位：米）："))
# vip_level = input("请输入你的VIP等级（1-5）：")
# if height <= 1.2 or vip_level in ['3', '4', '5']:
#     print("你可以免费入场！")
# else:
#     print("你需要购票入场！\n票价：50元")

#while循环练习
# while True:    #死循环
#     print("1")
#print(内容，end=结束符)  # end参数可以指定输出内容的结尾符号，默认是换行符\n
# print("1", end="")  # 输出内容不换行
# print("2")  
# print("3")
#   
#九九乘法表
#双层循环，内外分别控制行和列
# row = 1
# while row <= 9:
#     col = 1
#     while col <= row:
#         print(f"{col}*{row}={col*row}", end="\t")  # \t表示制表符，输出内容之间用制表符分隔
#         col += 1
#     print()  # 每行输出完后换行
#     row += 1

#for循环练习
# name = "aso ifjns adfnsk odfgo"
# count = 0

# for i in name:
#     if i == "a":
#         count += 1
# print(f"字符串中'a'的个数为：{count}")

# name = "123"

# for i in range(len(name)):
#     print(name[i],end = "")

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j}*{i}={i*j}", end="\t")
#     print()

