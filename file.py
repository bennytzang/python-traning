#儲存檔案
# file = open("data.txt", mode = "w",encoding = "utf-8") #開啟
# file.write("測試中文") #操作
# file.close() #關閉

# with open("data.txt",mode = "w",encoding= "utf-8") as file:
#     file.write("再一次測試")

# with open("data.txt",mode = "w",encoding= "utf-8") as file:
#     file.write("5\n3")

#讀取檔案
#把檔案數字資料讀出，並相加。
# sum = 0
# with open("data.txt", mode ="r", encoding="utf-8") as file:
#     for line in file: #一行一行的讀取
#         sum = sum + int(line)
# print(sum)

#使用 JSON格式讀取、複寫檔案
import json
# with open("config.json",mode = "r") as file:
#     data = json.load(file)
# print(data) #data是一個字典資料
# print("name", data["name"])
# print("version: ", data["version"])

#從檔案中讀取出JSON資料，放入變數data裡面
with open("config.json",mode = "r") as file:
    data = json.load(file)
print(data) #data是一個字典資料
data["name"] = "New Name" #修改變數中的資料
# 把最新的資料複寫回檔案中
with open("config.json",mode = "w") as file:
    json.dump(data,file)
