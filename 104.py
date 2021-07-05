# coding=utf-8
import smtplib
import sys
from email.mime.text import MIMEText                #專門傳送正文
from email.mime.multipart import MIMEMultipart      #傳送多個部分
from email.mime.application import MIMEApplication  #傳送附件

#寄件人資料
send_user='bennytzang0424@gmail.com'
password='creator0424'
#收件人資料，可為list
# receive_users=['bennytzang0424@gmail.com', 'bennytzang@gmail.com', 't105820036@ntut.org.tw','benny386@yahoo.com.tw']
receive_users = [input("輸入對方Email: ")]
# receive_users=['bennytzang0424@gmail.com']
# receive_users='benny386@yahoo.com.tw'
# receive_users='bennytzang0424@gmail.com'

subject='家教應徵信-臧英宏'           #郵件主題
email_text= "您好\n我在104家教網上看到您的應徵資訊，已經發送資料給您，同時在此寄送，感謝您閱信。\n我的名字是臧英宏。\n我目前就讀於國立臺北科技大學電子系研究所碩士班。\n◎專長：\n國中數學科、國中自然科、高中數學、高中物理\n◎教學經歷：\n教學經驗上擁有長達五年的教學經驗，自高中學測結束後便開始於板橋教育學院文理短期補習班擔任專職輔導老師，不管是一對一家教式教學、小班制課程與輔導、大型班級課程複習與習題檢討，均有多年經驗。\n◎教學方式：\n挑選合適參考書，配合自己製作的講義與考卷提供複習，將生活化例子帶入數學，引導公式推導與例題練習，再讓學生練習習題，誘導式學習，建立自信心，並檢討學校作業與考試；考前複習重點題型，並指導學生完成個人考前筆記，以利考前複習。\n視情況調整教學內容，上課前可有複習預習小考，並針對較需複習加強之章節多加練習。\n[現有三個家教案件，國一數學、高二數學物理、高三學測總複習，學生吸收效果良好。] \n\n以下為我的個人簡歷，方便您做參考\nhttps://drive.google.com/file/d/1jgQmWpV6cJpvfZSN5-Jr_XGQt94eydng/view?usp=sharing\n\n感謝您抽空閱信， 期待您的回應。\n祝   愉快   順心"
#server_address
server_address='smtp.gmail.com'
# server_address='smtp.mail.yahoo.com'
# server_address='smtp.ntut.edu.tw' #伺服器地址
mail_type='1'                   #郵件型別

def Send_Email():
    #創造一個郵件主體:正文/附件
    msg=MIMEMultipart()
    msg["From"]=send_user
    msg['To'] = (','.join(receive_users))
    # msg["To"]=receive_users
    # Header 接收的第一个参数的类型只能是字符串或者字节
    # 使用 join() 函数，将列表中字符串使用某种字符串连接，形式——str.join(list)
    msg["Subject"]=subject

    #正文內容構成
    part_text=MIMEText(email_text)
    msg.attach(part_text)           #將正文加入郵件體
    #附件內容構成
    # part_attatch1=MIMEApplication(open(file,'rb').read())                           #開啟附件
    # part_attatch1.add_header('Content-Disposition', 'attachment', filename=file)    #為附件命名
    # msg.attach(part_attatch1)       #新增附件
    #傳送郵件 SMTP
    smtp = smtplib.SMTP_SSL(server_address, 465)  #伺服器連線
    # smtp = smtplib.SMTP_SSL(server_address, 25)
    smtp.login(send_user,password)
    smtp.sendmail(send_user, receive_users, msg.as_string()) #傳送郵件
    smtp.close()
    print('郵件傳送成功!')

Send_Email()
# server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
# server.login("bennytzang0424@gmail.com", "creator0424")
# server.send_message(msg)
# server.close()

#添加附件 注意格式 'C:\\Users\\xxx\\xxx\\test.pdf'
#file ='C:\\Users\\TEST\\Downloads\\test.pdf'

#send_user = input("請輸入寄件人信箱: ")
#password = input("請輸入密碼: ")

# check = input("請再次確認，寄送請輸入  Y/y : ")
# if check =='Y' or check =='y':
#     Send_Email()
# else:
#     sys.exit()