#寄送 Email 的程式
#準備訊息物件設定
import email.message
msg=email.message.EmailMessage()
msg["From"]="bennytzang0424@gmail.com"
msg["To"]="bennytzang0424@gmail.com"
msg["Subject"]="測試信件"
#寄送純文字內容
# msg.set_content("純文字內容")
#寄送比較多樣式的內容
msg.add_alternative("<h3>優惠券</h3>滿五百送一百喔", subtype="html")
#連線到 SMTP Server, 驗證寄件人身分並發送郵件
import smtplib
#到網路上搜尋 gmail smtp server 或是 yahoo smtp server
server=smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login("bennytzang0424@gmail.com", "creator0424")
server.send_message(msg)
server.close()