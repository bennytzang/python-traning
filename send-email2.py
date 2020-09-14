import smtplib
from email.mime.text import MIMEText                #專門傳送正文
from email.mime.multipart import MIMEMultipart      #傳送多個部分
from email.mime.application import MIMEApplication  #傳送附件

#添加附件 注意格式 'C:\\Users\\xxx\\xxx\\test.pdf' 
file ='C:\\Users\\TEST\\Downloads\\test.pdf'    

#寄件人資料
send_user='bennytzang0424@gmail.com'
password='creator0424'
#收件人資料，可為list
receive_users=['bennytzang0424@gmail.com', 'bennytzang@gmail.com', 't105820036@ntut.org.tw']
# receive_users='benny386@yahoo.com.tw' 
# receive_users='bennytzang0424@gmail.com' 

subject='測試附加檔案'           #郵件主題
email_text='測試附加檔案'        #內文內容
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
    part_attatch1=MIMEApplication(open(file,'rb').read())                           #開啟附件
    part_attatch1.add_header('Content-Disposition', 'attachment', filename=file)    #為附件命名
    msg.attach(part_attatch1)       #新增附件
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