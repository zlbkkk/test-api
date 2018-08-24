#coding:utf-8
import smtplib
from email.mime.text import MIMEText
class SendEmail:
	# global send_user
	# global email_host
	# global password
	# global port
	# email_host = "smtp.163.com"
	# send_user = "18680674921@163.com"
	# password = "131539zlb"
	# port = 465
	def send_mail(self,user_list,sub,content):
		email_host = "smtp.163.com"
		send_user = "18680674921@163.com"
		password = "131539zlb"
		port = 465
		user = "Mushishi"+"<"+send_user+">"
		message = MIMEText(content,_subtype='plain',_charset='utf-8')
		message['Subject'] = sub
		message['From'] = user
		message['To'] = ";".join(user_list)
		try:
			smtp = smtplib.SMTP()
			smtp.connect(email_host)  # 连服务器
			smtp.login(send_user, password)
		except:
			smtp = smtplib.SMTP_SSL(email_host,port)
			smtp.login(send_user, password)  # 登录
		# server = smtplib.SMTP()
		# server.connect(email_host)
		# server.login(send_user,password)
		smtp.sendmail(user,user_list,message.as_string())
		smtp.close()

	def send_main(self,pass_list,fail_list):
		pass_num = float(len(pass_list))
		fail_num = float(len(fail_list))
		count_num = pass_num+fail_num
		#90%
		pass_result = "%.2f%%" %(pass_num/count_num*100)
		fail_result = "%.2f%%" %(fail_num/count_num*100)


		user_list = ['1315392407@qq.com']
		sub = "接口自动化测试报告"
		content = "此次一共运行接口个数为%s个，通过个数为%s个，失败个数为%s,通过率为%s,失败率为%s" %(count_num,pass_num,fail_num,pass_result,fail_result )
		self.send_mail(user_list,sub,content)

	# def send_mail(sender, psw, receiver, smtpserver, report_file, port):
	# 	'''第四步：发送最新的测试报告内容'''
	# 	with open(report_file, "rb") as f:
	# 		mail_body = f.read()
	# 	# 定义邮件内容
	# 	msg = MIMEMultipart()
	# 	body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
	# 	msg['Subject'] = u"自动化测试报告"
	# 	msg["from"] = sender
	# 	msg["to"] = receiver
	# 	# msg["to"] = ",".join(receiver)   只能字符串
	# 	msg.attach(body)
	# 	# 添加附件
	# 	now = time.strftime("%Y_%m_%d_%H_%M_%S")
	# 	att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
	# 	att["Content-Type"] = "application/octet-stream"
	# 	att["Content-Disposition"] = 'attachment; filename= "report.html"'
	# 	msg.attach(att)
	# 	try:
	# 		smtp = smtplib.SMTP()
	# 		smtp.connect(smtpserver)  # 连服务器
	# 		smtp.login(sender, psw)
	# 	except:
	# 		smtp = smtplib.SMTP_SSL(smtpserver, port)
	# 		smtp.login(sender, psw)  # 登录
	# 	smtp.sendmail(sender, receiver, msg.as_string())
	# 	smtp.quit()
	# 	print('test report email has send out !')

if __name__ == '__main__':
	sen = SendEmail()
	sen.send_main([1,2,3,4],[2,3,4,5,6,7])