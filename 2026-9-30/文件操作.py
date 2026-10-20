#文件操作
# f = open("C:/Users/9331x/Desktop/apex启动项.txt","r",encoding="utf-8")  #创建对象

""" content = f.read() #读取文件内容
print(content) 
print(type(content))     #打印内容
print(content.split(sep="\n"))   #按行分割内容
print(type(content.split(sep="\n")))  #打印类型
f.close()        #关闭 """


""" lst = f.readlines()  #读取所有行到列表
print(lst)           #打印列表
print(type(lst))  #打印类型
f.close()  #关闭文件 """


# for line in f.readlines(): 
#      line = line.strip()  #去掉每行的换行符
#      print(line)  #打印每行内容 

# f.close()  #关闭文件


""" num = 0
for line in f.readlines(): 
     line = line.strip()  #去掉每行的换行符
     if  "a" in line:
         num += 1

print("文件中包含a的行数为：",num)  #打印每行内容

f.close()  #关闭文件 """

f = open("1.txt","w",encoding="utf-8")  #创建文件
f.write("Hello, World!\n")  #写入内容 
f.flush()  #刷新缓冲区
f.close()  #关闭文件

f = open("1.txt","a",encoding="utf-8")  #打开文件
f.write("Additional content!")  #写入内容
f.flush()
f.close()  #关闭文件
