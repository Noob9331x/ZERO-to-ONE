""" try:
    f = open("non_existent_file.txt", "r")
except:
    f = open("non_existent_file.txt", "w")

f.close()  #关闭文件 """
try:
    open("123.txt", "r")
except FileNotFoundError as e:
    print("FileNotFoundError occurred:", e)